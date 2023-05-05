# 给 zotero 用的 kubikat 小工具
似乎 kubikat 官网给的 ris 需要配合他们的 filter 用 endnote 打开才能保证显示质量，直接导入 zotero 会有各种问题。

然而，那个 filter 质量实在不敢恭维，观察到有些地方存在信息的丢失。而且同时使用 zotero 和 endnote 总让人心里不爽……

仔细研究以后发现其实那个 ris 只是需要改变一下编码方式然后去除一些 “<<” 和 “>>”，再导入 zotero 就没什么问题了，于是随手用 python 写了个小工具来修改那个 ris。

反正也就是很简单的一个小工具，就当是方便过路人吧……
