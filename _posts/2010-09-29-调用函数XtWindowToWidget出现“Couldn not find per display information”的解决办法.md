---
layout: post
title: 调用函数XtWindowToWidget出现“Couldn't find per display information”的解决办法
date: 2010-09-29 20:00
categories: 编程
tags: 
---

　　在X11的桌面系统当中，如果你获得了Window ID（X11的Window类型），想获取对应的Widget，可以使用函数XtWindowToWidget。但是有时候会遇到错误“Couldn't find per display information”，出现这个错误的原因是因为传给函数XtWindowToWidget的参数Display是错误的。

<!-- more -->

　　在X11的源代码当中XtWindowToWidget函数到错误信息的调用堆栈是这样的：首先调用宏WWTABLE，在这个宏里面，调用了函数

_XtGetPerDisplay，进入函数_XtSortPerDisplayList，在这个函数里面，可以找到错误信息“Couldn't find per display information”。产生这个错误是因为传给XtWindowToWidget的参数display在全局变量_XtperDisplayList当中找不到。

　　只有函数XtOpenDisplay当中，才会把display会放到_XtperDisplayList里面去。一般来说，遇到这个错误的时候，display都是从XOpenDisplay（注意不是XtOpenDisplay）得到的，而函数XOpenDisplay是自己生成一个display，当然不会经过XtOpenDisplay往_XtperDisplayList里放一遍，实际上，倒是XtOpenDisplay先通过函数XOpenDisplay打开一个Display，然后再放到_XtperDisplayList的。所以，解决的办法就是用XtDisplay或者其他办法来获取一个display就可以了，一般来说，这都需要一个Widget作为参数，也是因此，如果只有一个Window ID，想获得对应的Widget是不可能的——至少，使用X11的函数是不太可能的。

　　上文中所有函数，都可以在网站http://www.xfree86.org/4.8.0/manindex3.html查到，X11 4.8.0源码下载：http://ftp.xfree86.org/pub/XFree86/4.8.0/source/

[原文在百度空间已经关闭]

