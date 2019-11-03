---
layout: post
title: Symbain菜鸟日记 May 2nd
date: 2010-05-02 20:00
categories: 编程
tags: Symbain
---


一个奇怪的new用法

　　原文叫做“replacement new”。作用是在制定的地址申请新的空间。比如下面：

<!-- more -->



int *p = new int;

int *q = new(p + sizeof(int)) int;

　　那么就可以确保q就是在p的后面。

　　或者：

unsigned char *heap = new unsigned char[1024];

int *p = new(heap) int;

 　那么p就是在heap上申请了四个字节的空间。

　　这种用法似乎没什么用处，也不太好，但是很新奇，我还真没试过。第一回听说。

[原文在百度空间已经关闭]

