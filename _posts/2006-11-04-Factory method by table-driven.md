---
layout: post
title: Factory method by table-driven
date: 2006-11-04 12:21
categories: 编程 
tag: C++ 
---
 
Maybe, discoverying or inventing factory mehtod by table-driven indenpended is the great summary of the first year of my programming way. I will write down how I think about this idea and I will give out a implemention of factory method by table-driven, in C++.
<!-- more -->
 
### Motivation

My first project is IFC. It is about Industry Foundation Classes (IFC), which is an international standard of construction industry. I can not tell too much about it, or else, I will leave a memory leak of the company’s secret. During this project, we will face to many classes, they form an inherited tree just likes MFC, but much more complex than MFC. I work out a framework to manage these classes, this framework works well when there is only 1 200 lines code in our project, also works well when the lines increase as many as 12 000 lines, and I have faith to say it will still work well even if there is 120 000 lines of code. But “works well” doesn’t mean there is no problem: in fact, I think the biggest problem is that if you add a new sub class, you need to first, add the declaration and definition of the class; second, create a instance of this new class and assign it to its base class pointer where it is used; third, add the unique identification of this class to two places and some very simple code, then the new sub-class will work as you want. 

Is it too complex to add a new class? Missing of any step will give out an unexpected result! When the project finished, I start to think about: How to make it easier to add a new class. We all know, in the three steps none will miss the first step, so if we can merge the rest two steps to the first step, then it will be easer (maybe easiest) to add a new class.
Intent

[原文来自我的教育网博客][原文来自我的教育网博客]

[原文来自我的教育网博客]:http://teacher.edu.cn/pc/article/200611/333820.html
