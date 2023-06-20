import sys, os, re, importlib, codecs, chardet
from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ctypes import *

font1 = QtGui.QFont()
font1.setPointSize(12) 

font2 = QtGui.QFont()
font2.setPointSize(11) 

def kubikat(file_path):
    
    str = file_path

    #处理编码问题
    f = open(str,"r",encoding = 'windows-1252')
    text = f.read()
    f.close()

    #处理多余的‘<<’和‘>>’
    text = text.replace('<<','')
    text = text.replace('>>','')

    #多行标题转写为一行
    text = re.sub('TI  - (.+)\nTI  - (.+)','TI  - \g<1>\n: \g<2>',text)

    #把译名作为笔记插入
    text = re.sub('TT  - (.+)\nTT  - (.+)','N1  - Translated Title: \g<1> : \g<2>',text)

    #让多个 AV 同时显示
    tmp = re.sub('AV  - (.+)\nAV  - (.+)\n','AV  - \g<1> ; \g<2>\n',text)
    while tmp != text:
        text = tmp
        tmp = re.sub('AV  - (.+)\nAV  - (.+)\n','AV  - \g<1> ; \g<2>\n',text)
    text = text.replace('AV  -','CN  -')

    #对 JOUR 和 CHAP 类型进行区分
    text = text.replace('JOUR','CHAP')
    text = re.sub('TY  - CHAP\n((.+\n)+)QS  - (.+)\((.+)','TY  - JOUR\n\g<1>QS  - \g<3>(\g<4>',text)

    #让多个 PB 同时显示
    tmp = re.sub('PB  - (.+)\nPB  - (.+)\n','PB  - \g<1> ; \g<2>\n',text)
    while tmp != text:
        text = tmp
        tmp = re.sub('PB  - (.+)\nPB  - (.+)\n','PB  - \g<1> ; \g<2>\n',text)

    #把 URL 作为链接存在
    text = text.replace('UR  -','L2  -')

    #把 SP 条目内容替换为 QS 条目内容
    text = re.sub('SP  - (.+)\nQS  - (.+)','QS  - \g<2>',text)
    text = re.sub('SP  - (.+)\n((.+)\n+)QS  - (.+)','\g<1>QS  - \g<4>',text)
    text = text.replace('QS','SP')

    f = open(str,"w",encoding = 'UTF-8')
    f.write(text)
    f.close()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.temp_list = []
        self.filter_paths = []
        self.paths_dictionary = []
        self.filter_names = []
        self.setWindowTitle('Zotero kubikat')
        self.setFixedSize(780, 460)
        #palette = QPalette()
        #palette.setColor(self.backgroundRole(), QColor(255,255,255))
        #self.setPalette(palette)
        self.setAcceptDrops(True) 

        # 拖入提示
        self.drag_note = QLabel(self)   
        self.drag_note.setText('把 RIS 文件拖入窗口或：')
        self.drag_note.setAlignment(Qt.AlignCenter)
        self.drag_note.move(580,30)
        self.drag_note.resize(150,50)
        
        # “导入文件”按钮
        self.RIS_files_chooser = QPushButton(self)
        self.RIS_files_chooser.setText("导入文件")
        self.RIS_files_chooser.move(580,70)
        self.RIS_files_chooser.resize(150,50)
        self.RIS_files_chooser.clicked.connect(self.file_choose)
        self.RIS_files_chooser.setFont(font1)
        
        # “导入文件夹”按钮
        self.RIS_folder_chooser = QPushButton(self)
        self.RIS_folder_chooser.setText("导入文件夹")
        self.RIS_folder_chooser.move(580,130)
        self.RIS_folder_chooser.resize(150,50)
        self.RIS_folder_chooser.clicked.connect(self.folder_choose)
        self.RIS_folder_chooser.setFont(font1)
        
        # 排列当前导入的所有文件
        self.paths_list = QListWidget(self)
        self.paths_list.move(50,60)
        self.paths_list.resize(500,340)
        
          
        # “开始处理”按钮
        self.start_button = QPushButton(self)
        self.start_button.resize(150,50)
        self.start_button.move(580,360)
        self.start_button.setText('开始处理')
        self.start_button.clicked.connect(self.start_translate)
        self.start_button.setFont(font1)
        #self.start_button.setStyleSheet('QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}')
        
        # “清除这条”按钮
        self.delete_this = QPushButton(self)
        self.delete_this.setText("清除这条")
        self.delete_this.move(580,240)
        self.delete_this.resize(150,50)
        self.delete_this.clicked.connect(self.delete_this_one)
        self.delete_this.setFont(font1)
        
        # “清空导入”按钮
        self.clear_paths = QPushButton(self)
        self.clear_paths.setText("清空导入")
        self.clear_paths.move(580,300)
        self.clear_paths.resize(150,50)
        self.clear_paths.clicked.connect(self.clear_all_paths)
        self.clear_paths.setFont(font1)
    
    def delete_this_one(self):
        item = self.paths_list.currentItem()
        self.paths_list.takeItem(self.paths_list.row(item))
    
    def clear_all_paths(self):
        self.paths_list.clear()
        self.paths_dictionary.clear()
    
        # 文件拖入事件
    def dragEnterEvent(self, event):
        event.acceptProposedAction()
        files = event.mimeData().urls()
        for tmp_file in files:
            tmp_file = tmp_file.toLocalFile()
            if re.match('.+\.ris', tmp_file):
                if tmp_file not in self.paths_dictionary:
                    self.paths_list.addItem(tmp_file)
                    self.paths_dictionary.append(tmp_file)
        
        # 导入文件方法
        
    def file_choose(self):
        
        self.temp_list = []
        self.temp_list = list(QFileDialog.getOpenFileNames(self, '选择文件' , '/', "RIS Files(*.ris)"))
        self.temp_list = self.temp_list[0]
        
        for tmp_path in self.temp_list:
            if re.match('.+\.ris', tmp_path):
                if tmp_path not in self.paths_dictionary:
                    self.paths_list.addItem(tmp_path)
                    self.paths_dictionary.append(tmp_path)
        
        # 导入文件夹方法
    def folder_choose(self):
        
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹', '/')
        
        folder_path = folder_path + '/'
        
        for file in os.listdir(folder_path):
            if re.match('.\.ris', file):
                if file not in self.paths_dictionary:
                    tmp_path = os.path.join(folder_path, file)
                    self.paths_list.addItem(tmp_path)
                    self.paths_dictionary.append(tmp_path)
        
        # 开始处理方法
    def start_translate(self):
       
        for tmp_path in self.paths_dictionary:
            kubikat(tmp_path)
        
        self.clear_all_paths()
        
        self.alert_message = QMessageBox(self)
        self.alert_message.setWindowTitle("提醒")
        self.alert_message.setStyleSheet("QLabel{"
                      "min-width:90px;"
                      "min-height:40px; "
                      "font-size:16px;"
                      "}")
        self.alert_message.setText("处理完毕")
        self.alert_message.resize(200,150)
        self.alert_message.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())