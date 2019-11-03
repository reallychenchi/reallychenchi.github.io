---
layout: post
title: Symbain菜鸟日记 Apr 18th
date: 2010-04-19 20:00
categories: 编程
tags: Symbain
---


　　如果编译报错“illegal use of incomplete struct/union/class 'CContactItem'”，那么问题很可能是因为类CContactItem的头文件没有添加到这个cpp文件里面来。编译器报错的方式还真不一样，如果是Visual C++编译器报错，大概是xxx undefine之类吧。这个问题很奇怪，如果是没有定义，那么确实塞班的也会报一个Undefine出来，但是为什么又有一个illegal use？原因可能是因为其他地方有对类CContactItem的前置声明，所以不是未定义吧？

<!-- more -->



　　还有一个奇怪的现象是，我的程序突然出现了在模拟器当中退出时候报内存错误的现象，是在堆上面存在内存泄漏。而且如果是进入通讯录退出，也有一样的问题——这就不正常了，通讯录是模拟器里面自带的，又不是我写的。我观察过电脑的内存，不可能存在内存不足的问题。可能是和新调用的类相关吧，也需要再试试看。

　　崩溃的一天。

[原文在百度空间已经关闭]

