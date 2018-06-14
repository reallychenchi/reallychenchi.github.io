---
layout: post
title:  "智力游戏-将帅问题"
date:   2012-09-18 09:42:14 +0800
categories: 编程
tags: 算法 编程之美
---
　　编程之美的第二题，是要求“只用一个变量”打印出将帅所有合法的位置。这个题目不加限制的话一点也不难，加了限制就要动动脑子了。
 <!-- more -->

　　我的思路是，将、帅的位置各自有9种，那么一共就是81种组合，那么就定义变量在for循环里表示81种组合，用除法和取余来区分各种状态。代码写出来也很简单（因为不用变量啊！）　　

　　Python代码实现如下：

{% highlight python %}
for i in range(0, 81):
	if (int(i / 9) % 3) == ((i % 9) % 3):
		continue
	print(chr(int(i / 9) % 3 + ord("d")), int(int(i / 9) / 3) + 1, " - ", chr((i % 9) % 3 + ord("d")), int((i % 9) / 3) + 1)
{% endhighlight %}

　　i/9和i%9就分别表示将和帅的位置，%3是表示他们的纵坐标，他们纵坐标是不能一样的，这样就把不合法的情况去除掉了。后面那个print纯粹就是用来输出而已：

{% highlight python %}
d 1 - e 1
d 1 - f 1
d 1 - e 2
d 1 - f 2
d 1 - e 3
d 1 - f 3
e 1 - d 1
e 1 - f 1
e 1 - d 2
e 1 - f 2
e 1 - d 3
e 1 - f 3
f 1 - d 1
f 1 - e 1
f 1 - d 2
f 1 - e 2
f 1 - d 3
f 1 - e 3
d 2 - e 1
d 2 - f 1
d 2 - e 2
d 2 - f 2
d 2 - e 3
d 2 - f 3
e 2 - d 1
e 2 - f 1
e 2 - d 2
e 2 - f 2
e 2 - d 3
e 2 - f 3
f 2 - d 1
f 2 - e 1
f 2 - d 2
f 2 - e 2
f 2 - d 3
f 2 - e 3
d 3 - e 1
d 3 - f 1
d 3 - e 2
d 3 - f 2
d 3 - e 3
d 3 - f 3
e 3 - d 1
e 3 - f 1
e 3 - d 2
e 3 - f 2
e 3 - d 3
e 3 - f 3
f 3 - d 1
f 3 - e 1
f 3 - d 2
f 3 - e 2
f 3 - d 3
f 3 - e 3

{% endhighlight %}

　　其实不难，难的还在后面

[原文来自我的教育网博客][原文来自我的教育网博客]

[原文来自我的教育网博客]:http://teacher.edu.cn/pc/article/201209/557285.html
