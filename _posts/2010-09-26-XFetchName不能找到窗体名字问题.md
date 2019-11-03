---
layout: post
title: XFetchName不能找到窗体名字问题
date: 2010-09-26 20:00
categories: 编程
tags: Delphi
---


　　XFetchName在X11lib当中是用来获取窗体名字的，具体的使用方法，可以参考：http://www.helplinux.cn/man/3/xsetwmname.html

　　在使用这个函数来获取窗体名字的时候，会发现很多窗体获取不到。经过测试，发现父窗体都是可以找到的，但是子窗体完全都找不到。我猜测，原因在于XFetchName是用来获取窗体Title的，所以子窗体没有，父窗体却有。

<!-- more -->

　　在这种情况下，可以试试看函数XtName（http://www.xfree86.org/4.8.0/XtName.3.html），如果你只有Window的变量，那么可以使用函数XtWindowToWidget（http://www.xfree86.org/4.8.0/XtWindowToWidget.3.html）转换成Widget。因为这种情况下，很可能是在创建Widget的时候传入了name显示出来的（函数XtCreateWidget，http://www.xfree86.org/4.8.0/XtCreateWidget.3.html）

[原文在百度空间已经关闭]

