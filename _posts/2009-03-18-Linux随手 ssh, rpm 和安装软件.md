---
layout: post
title: Linux随手 ssh, rpm 和安装软件
date: 2009-03-18 20:00
categories: 扯闲篇
tags: Linux
---


Linux老师要我们编译一个Linux内核出来，编不出来，就有好看～～～吓得我连忙找东西编。一点点东西，记下来。

1. 启动Linux当中SSH服务的命令是

<!-- more -->



/etc/rc.d/init.d/sshd start

查询是

netstat -a > a.txt

如果存在下面的行，说明SSH服务已经建立

tcp    0       0 *:ssh          *:*          LISTEN

2. rpm的安装命令是rpm -ivh [rpm包名字]

这个包名字可以是本机目录，也可以是远程目录，比如：

rpm -ivh http://download.fedora.redhat.com/pub/fedora/linux/releases/10/Fedora/i386/os/Packages/gcc-4.3.2-7.i386.rpm

或者

rpm -ivh gcc-4.3.2-7.i386.rpm

3. 获取安装rpm包文件，可以从网址http://download.fedora.redhat.com/pub/fedora/linux/releases/10/Fedora/i386/os/Packages/

中获得，其中的/10/Fedora是表示第十版Fedora

 

[原文在百度空间已经关闭]

