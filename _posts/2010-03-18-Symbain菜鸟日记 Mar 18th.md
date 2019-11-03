---
layout: post
title: Symbain菜鸟日记 Mar 18th
date: 2010-03-18 20:00
categories: 编程
tags: Symbain
---


 

　　诺基亚的开发资料还真齐全，找到一个类似MSDN的地方：

　　http://library.forum.nokia.com/

<!-- more -->



　　不过也真是灯下黑，这个我应该最开始就发现才对啊。在某种程度上说，比MSDN更好，比如下面这个：

http://www.forum.nokia.com/info/sw.nokia.com/id/f63ebb0a-3cee-4a02-b4f6-6c9090bfddc9/S60_5th_Edition_Mobile_Paint_Example.html

　　居然还有视频解说。虽然我电脑太慢看不了，但是诺基亚的这份心意，我还是心领了（不心领还有啥法儿？）

　　CFbsBitmap真难用，可能是因为我还没入门吧，折腾啊。不过折腾也是有回报的：

　　军规第一条：调用CFbsBitmap除了添加头文件fbs.h以外，还需要添加库fbscli.lib，尤其是在报错说“

CFbsBitmap::CFbsBitmap() undefined”的时候。

　　都是用Visual C++的MFC给惯的，连这么简单的问题都忘记了，类声明找不到加头文件，函数定义找不到加库文件。我是说我自己。

　　军规第二条：在Carbide.vs当中，如果想调试的时候设置断点，那么请在按下F5之前设置好断点。我尝试的结果是如果在开始调试以后设置断点，是无效的。

　　这个是没地方教，自己摸索的。我猜测是Carbide.vs的处理导致的，表面上我们调试的是自己的代码，实际上，我们调试的是模拟器，所以在开始调试以前设置的断点才有效，而以后的就无法生效了。还是不错的，至少能调试，很好。

　　我是参考一份www.mopius.com编写的简单入门来做的，虽然这份文档里面有些地方可能和版本不太符合，但是其中的思路很棒，文件的名字就是“GettingStartedWithCarbideVS.pdf”，推荐一下。

[原文在百度空间已经关闭]

