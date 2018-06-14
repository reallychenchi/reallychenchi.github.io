---
layout: post
title:  "智力游戏-控制CPU利用率"
date:   2012-09-17 05:05:14 +0800
categories: 编程
tags: 算法 编程之美
---
　　《编程之美》是一本很好的书，里面的题目很有意思。第一道题目就是控制CPU利用率并且显示一个正弦函数。今天做了一下这个题目，放上来给大家共享。

　　思路是控制CPU利用率，那么就在线程里面，交替线程挂起或者执行运算，通过分配挂起和运算的时间片来改变利用率：如果需要50%，那么就挂起时间和运算时间相等；如果需要5%，那么挂起时间和运算时间比例为19:1好了。运算时间，我们是不能控制的，就控制线程挂起时间。
 <!-- more -->

　　控制线程挂起时间用定时器恐怕精度不够，而且我用的语言是Python，还不知道对定时器支持如何呢！所以我采用的办法是让线程进入循环，每次循环都获取毫秒为单位的时间值，模100以后，判断是否大于当前需要的百分比，如果大于就挂起，否则就执行一个乘法运算。这个算法不太好，因为这样挂起时间和运算时间分配太开了，在一秒以内是完全分开的。好一点的算法是挂起时间和运算时间尽量均匀一些，但是又不要占用太多运算资源。

　　针对单核CPU，Python代码如下：

{% highlight python %}
import time
import threading
import math

class EatCpuQuater(threading.Thread):
	percent = 0
	NUM = 100;

	def run(self):
		while(self.NUM < 101):
			start = time.time() * 100
			ti = int(start)
			tim = ti % 100
			if tim >= (100 - self.NUM):#判断是否需要挂起线程
				time.sleep(0.03)#挂起线程0.03秒
			else:
				self.percent = self.percent * 31#执行一次运算


	def setPercent(self, p):#设置CPU利用率
		self.percent = p
		self.NUM = 100 - self.percent;

def f(i):#在这里指定函数
	r = math.sin(i / 100.0 - 0.87) * 50.0 + 50.0
	return int(r)

e = EatCpuQuater()
e.start()
for i in range(0, 8000):
	e.setPercent(f(i))#设置 CPU利用率
	time.sleep(0.5)#每0.5秒重置一下CPU利用率

e.setPercent(-1)#退出程序
{% endhighlight %}

　　在使用低刷新率情况下效果不错，画出来的效果如下：

![PNG](/assets/img/2012-09-17-beauty-of-pp-control-cpu-p1.png)


　　有些毛刺，但是大体还说得过去。用Python恐怕很难消除这些毛刺了。

　　原文的题目，进一步，提出对于多核怎么处理？这个说简单也简单，有几个核，就开几个线程好了，所有的线程做一样的事情（不需要完全一样），就可以了。

　　按照这个思路，我修改了主函数代码如下，其他代码没有改动：

{% highlight python %}
lst = []
e = EatCpuQuater()
e.start()
lst.add(e)
e = EatCpuQuater()
e.start()
lst.add(e)
e = EatCpuQuater()
e.start()
lst.add(e)
e = EatCpuQuater()
e.start()
lst.add(e)
for i in range(0, 2000):
	for e in lst:
		e.setPercent(f(i))
	time.sleep(0.1)

for e in lst:
	e.setPercent(-1)
{% endhighlight %}

　　改动仅仅在于后面又多启动了几个线程。但是说难也真难，因为对于Python和Java这样的语言，恐怕不是这么一回事儿，因为它们的线程是虚拟机控制的，比如Python的就根本不支持多核，任凭你多少线程，它只占一个核，所以上面我的代码其实是不管用的。那怎么办？

　　办法还是有的，可以同时跑四个Python程序，每个程序都是前面的单核代码。但是这样我试了试效果很不好，大概是Python虚拟机也要占用一部分CPU的原因。我想，如果是用C++可能效果会好一些，不过也难说，这个还取决于Windows是怎么分配线程到CPU处理器呢。

[原文来自我的教育网博客][原文来自我的教育网博客]

[原文来自我的教育网博客]:http://teacher.edu.cn/pc/article/201209/557136.html
