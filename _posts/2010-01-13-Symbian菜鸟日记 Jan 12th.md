---
layout: post
title: Symbian菜鸟日记 Jan 12th
date: 2010-01-13 20:00
categories: 编程
tags: Symbian
---


　　虽然苹果黑莓日盛一日，诺基亚江河日下，不过我是坚定的诺记拥趸，尽管心里觉得索尼爱立信的手机比诺基亚的更好点。有一个小应用需要用塞班做，就把中间过程记录下来做个历史吧——谁知道塞班有多少明天呢？

<!-- more -->



0. 下载和安装SDK

　　这个没什么好说的，我下载的网址是：

http://www.forum.nokia.com/info/sw.nokia.com/id/4a7149a5-95a5-4726-913a-3c6f21eb65a5/S60-SDK-0616-3.0-mr.html

　　这里所有的版本都有了，如果你不知道自己的手机对应是什么版本SDK，可以到下面网址查找：

http://developer.symbian.com/china/tools_and_sdks/sdks/s60/

1. 开发环境的搭建

　　对于初步上手的人，有一个集成开发环境是很重要的。命令行很酷很高效，但是刚开始菜鸟扑腾，酷有啥用？（切身的深刻教训：刚刚开始学，先整个集成开发环境）。

　　塞班开发的集成开发环境比较好的是Carbide。首先这是诺基亚首推的。Carbide C++下载的地址是：http://www.forum.nokia.com.cn/sch/main/carbide.html。据说也有Carbide Java，但是我没找到。

　　如果你是用Java的，那么可以在这里：http://www.forum.nokia.com/Tools_Docs_and_Code/Tools/IDEs/

　　看看，这里把基本上所有支持的集成开发环境都列出来了。

　　另外说一句，Carbide C++是基于Eclipse的，对于用惯了Eclipse的程序员，或者目前没什么特定习惯集成环境的，选择Carbide C++很好。但是如果习惯了VS的呢？

　　Carbide.vs，可惜诺基亚已经不支持了，所以在诺基亚的官方网站是下载不到了。如果你的VS是2003，需要下载Carbide.vs 2.0，在

http://download.csdn.net/source/1934180　

http://download.csdn.net/source/1934188

　　如果是VS2005，需要下载Carbide.vs 3.0，在：

http://download.csdn.net/source/943670　

http://download.csdn.net/source/943672　

　　在安装的时候，会找你要注册号。那么到诺基亚论坛（https://www.forum.nokia.com/Sign_Up.xhtml）注册一个账号就可以了，安装时候要求注册号的时候选“I have a internet connection”，然后会自动打开一个页面，填上你的账号和密码就可以了。

　　下载以后还需要一些事先安装，可以参考：

http://www.forum.nokia.com/Tools_Docs_and_Code/Tools/IDEs/Carbide.c++/

http://www.cnblogs.com/peterzb/archive/2009/06/11/1501559.html

　　完成上述步骤，开发环境就搭建起来了。我用的是Carbide.vs 2.0/C++/VS2003。

2. 下载一本手册：

　　这个，就随便找找好了，中文的最好。辅助以SDK里的帮助文档。就从经典的Hello World开始吧！

[原文在百度空间已经关闭]

