# 给 Zotero 用的 kubikat 小工具
似乎 kubikat 官网给的 ris 需要配合他们的 filter 用 Endnote 打开才能保证显示质量，直接导入 zotero 会有各种问题。

然而，那个 filter 质量实在不敢恭维，观察到有些地方存在信息的丢失。而且同时使用 Zotero 和 Endnote 总让人心里不爽……

仔细研究以后发现其实那个 ris 只是需要改变一下编码方式然后对内容做一些修正，再导入 zotero 就没什么问题了，于是随手用 python 写了个小工具来修改这个 ris。这样只要在导入之前用这个工具修正一遍就可以直接导入 Zotero 了。

### 说明：
1. 采用“主标题 : 副标题”的方式来显示副标题。
2. 译名放进了笔记（如果有的话），格式同1.
3. 存档位置如果有多个，用分号隔开。
4. 原始数据的 QS 行实在没地方存，存放到 CN（索书号）里面了。

*.exe 文件供 Windows 使用，无后缀的 Unix 可执行文件供 MacOS 使用。

直接运行，然后输入文件路径。在同一目录下面的话输入文件名就行，不同目录的话要把绝对路径输入进去。
