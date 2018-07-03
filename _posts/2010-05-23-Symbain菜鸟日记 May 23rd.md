---
layout: post
title: Symbain菜鸟日记 May 23rd
date: 2010-05-23 20:00
categories: 编程
tags: Symbain
---


　　把The Accredited Symbina Developer Primer Fundaments of Symbain OS（好长）看完了，做个总结吧：

　　书是好书，一点不假，非常合适入门；

<!-- more -->



　　Symbain的不同之处，在于紧紧围绕着资源二字做文章，尤其是内存。

　　在Symbian当中，使用动态数组来操作数量不同的对象，Dynamic Array；

　　可以用不同的线程来完成多线程操作，但是推荐使用Active Object，同样是为了节省资源，内存和CPU资源。

　　线程间通信可以使用IPC；

　　Client-Server是一个比较典型的应用，但是如果可能，应该尽量减少客户端对服务器端的调用，也是为了节约资源；

　　在Symbain当中操作文件，可以直接使用Client-Server，也可以通过流来使用。后者是推荐的，因为流已经对服务器端调用做了封装和优化，可以减少调用次数。流用起来也方便一些。

　　

[原文在百度空间已经关闭]

