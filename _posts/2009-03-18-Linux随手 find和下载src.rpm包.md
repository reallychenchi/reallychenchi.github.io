---
layout: post
title: Linux随手 find和下载src.rpm包
date: 2009-03-18 20:00
categories: 扯闲篇
tags: Linux 
---


1. find命令

　　作用是查找一个文件，ls只能查找单层的文件，但是用find，就可以查找嵌套很多目录的文件，命令格式是：find / -name xxxx.xxxx，比如find / -name sshd

<!-- more -->



2. src.rpm包

　　这样的包是redhat的源代码发行包，可以在http://download.fedora.redhat.com/pub/fedora/linux/releases/10/Fedora/source/SRPMS/下面找到，其中，Fedora10用的Linux内核包是kernel-2.6.27.5-117.fc10.src.rpm

　　使用方法是首先用rpm -Uvh kernel-2.6.27.5-117.fc10.src.rpm命令解压缩rpm包

　　然后找到（用find命令）spec文件

　　接着执行rpmbuild -bp --target $(uname -m) kernel-2.6.spec命令，注意，这个命令是要在root权限下执行的。如果是普通用户，需要先执行uname -m，获得输出，然后再执行rpmbuild，比如在我的虚拟机上是i686，那么就应该是rpmbuild -bp --target i686 kernel-2.6.spec

　　开始时候，我用的是老师提供的Fedora5的src.rpm包，但是编译的时候那叫一个不顺利，显示spec文件坏掉了，有一行重复（你觉得Linux的会犯这种错误吗？），然后是编译时候说这不能用了那出错了……这、这、这、发布的时候，难道他们没有调试吗？

　　说实话，我很怀疑，老师对给我们的包做了手脚，以免我们不努力。。。

　　编译时候，可能说这个没有，那个版本不够，那么，就用上一篇当中的rpm和下载目录，找到以后下载安装。

　　今天晚了，开着电脑编译着，小陈我睡觉去了，困啊～～～

[原文在百度空间已经关闭]

