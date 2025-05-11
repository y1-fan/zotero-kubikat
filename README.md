# 给 Zotero 用的 kubikat 小工具

### 2025/5/11 重要说明：

近期 kubikat 给自己的数据库进行升级，然而结果不尽如人意，主要有以下几方面需要注意：

1. 引入了登录机制，并且不存在注册选项。依 Zentralinstitut für Kunstgeschichte 提供的[说明](https://www.zikg.eu/bibliothek/benutzung-und-service/bibliotheksausweis)，应该必须线下办理图书馆卡才能登录 kubikat。目前，如果要选择某一搜索结果的所有条目进行导出，就必须进行登录，否则只能按页导出（每页最多显示 50 条）。
2. 当前的导出的格式全部都存在重大的问题：
   1. 用 EXCEL/CSV 进行导出能够获得最丰富的信息，但是参考文献类型全面缺失，无法进行有效的文献管理。
   2. RIS 勉强算是保留了文献类型，但是信息缺失极其严重，很多文献只剩下了标题、作者和年份。
   3. EndNote 导出选项与之前的导出一致，但是添加了在 Clarivate 云端的 EndNote 上进行导入再导出的步骤。
   4. BibTeX 最为混乱，不仅文献类型错误严重，保留了原方法中的乱码，而且还缺失信息。

我已就一些问题向 kubikat 方面的人进行了咨询。依据 Zentralinstitut für Kunstgeschichte 网站上有关这次更新的[文章](https://www.zikg.eu/aktuelles/nachrichten/go-live-des-neuen-kubikat-katalogs)的说法：

>Wir weisen darauf hin, dass in den ersten Tagen nach dem Go-live noch Konfigurationsprozesse laufen, bis alle Daten in der gewünschten Form dargestellt werden. Dies betrifft u.a. die Anzeige von E-Books und Zeitschriftenbeständen.
>我们在此提醒您，系统上线后的最初几天仍需进行配置流程，直至所有数据都能以所需形式呈现。此过程尤其涉及电子书及期刊馆藏的显示问题。

期待馆方在未来能够解决一些问题。

---

似乎 kubikat 官网给的 ris 需要配合他们的 filter 用 Endnote 打开才能保证显示质量，直接导入 Zotero 会有各种问题。

然而，那个 filter 质量实在不敢恭维，观察到有些地方存在信息的丢失。而且同时使用 Zotero 和 Endnote 总让人心里不爽……

仔细研究以后发现其实那个 ris 只是需要改变一下编码方式然后对内容做一些修正，再导入 zotero 就没什么问题了，于是随手用 python 写了个小工具来修改这个 ris。这样只要在导入之前用这个工具修正一遍就可以直接导入 Zotero 了。

### 说明：

1. 采用“主标题 : 副标题”的方式来显示副标题。
2. 译名放进了笔记（如果有的话），格式同1.
3. 存档位置如果有多个，会用分号隔开。
4. 原始数据的 QS 行实在没地方存，存放到 CN（索书号）里面了。

~~*.exe 文件供 Windows 使用，无后缀的 Unix 可执行文件供 MacOS 使用。~~

~~直接运行，然后输入文件路径。在同一目录下面的话输入文件名就行，不同目录的话要把绝对路径输入进去。~~

（已经有 GUI，不需要再手动输入路径了。下载移步 Release）

---

### 2023/5/12 Update：

1. 添加多出版社支持。
2. 优化 URL 的放置位置。
3. 更正部分 Book Section 和 Journal 类型混淆的情况。
4. QS 行数据存放位置改为 SP.

### 2023/6/20 Update：

1. 存档位置中的内容挪至索书号（CN）。
2. 增加 GUI，操作应该会更加方便。
