---
layout: post
title:  "博客建设后记"
date:   2018-06-11 20:07:14 +0800
categories: 编程
---

终于一篇一篇的把以前放在百度空间和教育网博客的文章迁移过来，确实是人工不如自动化，迁移个博客，还写了写Python的网络爬虫。

<!-- more -->

### 教育网博客的自动迁移

其实要算半自动。首先到教育网博客的主页那里，按照年份把网页另存下来，然后执行 [教育网爬文章工具][edubloger] 就会自动生成_post目录下面的md文件了，但是还要手工分段。

尽管如此，效率也比一篇一篇的慢慢挪强多了。

### 百度空间的自动迁移

这就基本自动化了。

首先用浏览器打开百度文章，查看cookie内容，把 [百度脚本][baidufetcher] 里面的对应项都改掉，然后执行这个脚本，就把百度文章里面的全部内容，包括图片都抓取到本地了。但是在本地也不能用，这时候就要执行 [百度文章爬虫工具][baidubloger] 就自动生成出来md文件了，基本不用手工修改。

不过为了设置标签和分类，其实还是手工过了一遍的，不过确实比完全手工操作强多了，两三百篇全手工操作要到明年了。

感谢 [imdjh][github] 制作了抓取百度文章的脚本。

[edubloger]: /assets/edublogMover.py 
[baidubloger]: /assets/baiduMover.py 
[baidufetcher]: /assets/baidu.sh
[github]: https://github.com/delight09/gadgets/blob/master/network/yunwenzhang_pirater.sh

