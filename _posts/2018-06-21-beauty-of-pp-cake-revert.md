---
layout: post
title:  "智力游戏-翻烧饼"
date:   2018-06-21 14:54:00 +0800
categories: 编程
tags: 算法 编程之美
---

第三个题目是要求只使用翻烧饼的方式，把一摞烧饼整理成小烧饼在上面大烧饼在下面的顺序，当然，要求最少翻动次数。

那么可以简化问题为对烧饼的半径排序，只考虑实现的Python代码如下：
 <!-- more -->

{% highlight python %}
import random

def revertCakes(cakes, start, end):
    for i in range(start, (start + end) / 2):
        tempCake = cakes[i]
        cakes[i] = cakes[end - (i - start) - 1]
        cakes[end - (i - start) - 1] = tempCake

def sortCakes(cakes, start, end):
    #No need to sort for only one element
    if start == end:
        return
    #Find the max cake
    bottomCakePos = start
    for i in range(start + 1, end):
        if cakes[i] > cakes[bottomCakePos]:
            bottomCakePos = i
    #Put max cake to bottom
    revertCakes(cakes, start, bottomCakePos + 1)
    revertCakes(cakes, start, end)
    #Sort the rest cakes
    sortCakes(cakes, start, end - 1)

#Create random cakes
cakes = range(10)
for i in cakes:
    cakes[i] = random.randint(1, 20)
print "Before sort:"
for r in cakes:
    print r
sortCakes(cakes, 0, len(cakes))
print "After sort:"
for r in cakes:
    print r
{% endhighlight %}

这里的排序其实就是简单的冒泡排序，一次交换由两次翻动代替。要求最少的翻动顺序，一方面可以考虑使用快速排序的思路；另外一方面需要考虑是否可能针对翻动这个操作进行特殊的优化。

