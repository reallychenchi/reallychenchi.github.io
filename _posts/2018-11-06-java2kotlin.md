---
layout: post
title:  "Java to Kotlin"
date:   2018-11-06 14:54:00 +0800
categories: 编程
tags: Kotlin
---

Kotlin确实是全面兼容Java的，但是也有一些不一样的地方，如果不注意很容易造成误解。

### class.java vs javaClass
 <!-- more -->

在绑定服务的时候，开始是这样写的：
{% highlight java %}
var bindIntent = Intent(this@BaseActivity, DataService::javaClass.javaClass);
{% endhighlight %}
无论如何也不能成功，后来发现应该这样写：
{% highlight java %}
var bindIntent = Intent(this@BaseActivity, DataService::class.java);
{% endhighlight %}

存在两个问题：

1、为什么第一种做法写一个javaClass提示错误，这样写两个就编译通过了？

2、为什么第二种可以用，第一种不能用？

### inner class

在Java当中，默认就是内部类，如果要声明静态类需要使用static关键字。但是Kotlin当中修改为默认就是静态类，需要声明内部类才使用inner关键字。

当程序员误以为自己声明了一个内部类，试图引用外部类的this对象，写出this@的时候，并没有任何提示，对Java程序员是一个不大不小的困扰。这样的改动并非只有这一处，比如默认的类都是不可继承的，但是当程序员试图继承一个类的时候，Idea会提示把类改为Open模式，避免了这种修改可能导致的问题。


