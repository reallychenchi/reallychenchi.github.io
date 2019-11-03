---
layout: post
title: 关于IFC文件读取类的设计的想法（LocalPlacement）
date: 2006-01-11 03:09
categories: 编程
tags: IFC
---

　　IFC文件是用树形结构组织的，LocalPalcement也是通过树形结构来实现一层一层的递归嵌套的相对坐标系统。那么，假设我们需要把这个相对坐标系统中的点转换成为一个只有一个绝对坐标系统的点，类的设计应该考虑增加一个堆栈，保存所有的LocalPlacement。在转换的时候，可以逐个调用。

<!-- more -->

　　在这个堆栈中，所存储的对象应该是一个LocalPlacement对象，它存储了一个相对坐标，包括Direction、相对原点和一个负责把坐标系内外的点互相转换的函数，或者两个函数。

IFC files are orgnaized like a tree. The LocalPlacement is also orgnaized like a tree, and a relative coordinate system is created like this. Then, suppose we need to convert a point in the relative coordinate system in IFC to a univerisy coordinate system, I think we should consider to add a stack, which store all the LocalPlacement. When we covert the point, we can convert from one coordinate to another one by one, and after we finished all the coordinate, we convert a point in relative coornidate system to a point in uinverity coornidate system.

Inside this stack, it should be a object of LocalPlacement, which contains the Direction of its coordinate system, the origin point of its coordinate system and one function respond for covert points into its coordinate system, another function respond for convert points out of its coordinate system.

[原文来自我的教育网博客][原文来自我的教育网博客]

[原文来自我的教育网博客]:http://teacher.edu.cn/pc/article/200601/333804.html
