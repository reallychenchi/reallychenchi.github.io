---
layout: post
title: To replace in VIM
date: 2008-07-08 20:00
categories: 编程
tags: VIM 
---
VIM is a wonderful editor for text files. I like the style of VIM, without any operation of mouse, just typing fast in the keyboard, then everything is done! That does feel good. Of course, if you are not good at typing nor you do not like many many commands, surely you will not like VIM.

<!-- more -->

But some commands in VIM are hard to use correctly, not because it's complex, but because it's ambiguous. To replace in VIM is a sample. You can refer to this link http://zhidao.baidu.com/question/26269661.html?si=1

In fact the command should be %s/old/new/gc. The detail explain as follow:

     * s means to substitute, default range is the current line;

     * The first word after slash is the word to be replaced;

     * The second word after slash is the word to replace;

     * /g means that all the occurence of old word in the range should  be replaced;

     * /c means confirm before replace;

     * % means that the range is the whole text file.



Most people forgets the %, including the one in baidu, then VIM will only search in the current line, so "Pattern not found" will jump out. I make such mistake for many times, too.

[原文在百度空间已经关闭]

