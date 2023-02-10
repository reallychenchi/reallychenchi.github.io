---
layout: post
title: Chatgpt走进面试间
date: 2023-2-11 02:37
categories: 编程
tags: Chatgpt
---
看了[Chatgpt通过谷歌面试的新闻][news]以后，我暗中冷笑不已：什么年代了，还用leetcode这种机械的面试题，活该如此！Chatgpt幸亏没开放大陆使用，否则落在我的手里，要你好看！

 <!-- more -->

# 要你好看！

早年间我觉得leetcode面试还不错，有空自己也喜欢去刷，找到感觉了刷得还挺来劲。偶尔忝列面试官的时候也会出leetcode的题目，但是只用easy题目，我觉得hard题目已经不是考察编程能力了，而是考察背题能力。最常用的是这个：

一个数组长度为[2n + 1]，包括n+1个数字，其中只有一个数字是单独出现，其他数字都会出现两次，例如[1, 2, 2, 1, 3] ，请找出只出现一次的数字。

它的好处在于：

1、很简单，写不出来直接拉黑送走；

2、次优解可以从时间复杂度也可以从空间复杂度上优化，有讨论空间，能做到这一步就可以通过了；

3、最优解还能做出来的应该是做过原题的，能讲清楚原理（位运算）的必然计算机基础扎实，给个高分应该；如果讲不清楚原理结合其他情况可以判断出来是作弊的也拉黑送走；

4、给出最优解的还可以扩展一下，如果长度是3n+1要怎么做？

这道题适合应届生，Chatgpt来做肯定能给出最优解，但是第四部的扩展应该是搞不定的，这是我自己想的，网上没有。

对于工作三五年的再用这个题目就不合适了，我常用的是从知乎上看到的一个面试题：要求写一个类来表达数学上的”分数”，可以加减乘除、用作hashCode、转换成字符串和约分，比如2/3、8/13等等，不允许用辗转相除做约分。它的好处在于：

1、这是一个设计题，可以考察候选人的设计能力而且可以在20分钟左右完成；

2、可以考察数学基础能力，有不少英雄汉倒在加减乘除上；

3、分子、分母是否是用public final、分母为0的处理、hashCode和equals上等可以看出编程习惯；

4、如果用工厂方法代替构造函数应该是看过effective java的，可以展开；

5、加减乘除需要两个分母相乘，这时候的溢出处理就比较费脑子了；

6、toString的时候边界条件处理上也可以看出来细心程度。

这个题目交给Chatgpt的话，辗转相除应该会做，但是其他应该是不行的，毕竟这是一个主观题。

# 看得目瞪口呆

我注册了一个chatgpt以后感觉很好用，想起来那个新闻之后觉得chatgpt是一个检查面试题好坏的标准：如果chatgpt都能做出来的面试题，肯定不是什么好面试题，好的面试题是chatgpt做不出来的面试题。

为了验证一下我自己的这两道题有多好，我把它出给了chatgpt，不然怎么：“要你好看！”。

## 第一题的扩展

第一题不用说，原题直接给出了最优解，这是意料之中的。

但是我对自己的扩展题目还是很有信心的，没想到的是……chatgpt给出来了最优解，必须S。

题目：一个数组长度为[3n + 1]，包括n+1个数字，其中只有一个数字是单独出现，其他数字都会出现三次，例如[1, 2,  2,1, 1, 2, 3] 。请找出只出现一次的数字。

回答

{% highlight java %}
    public static int findSingleNumber(int[] arr) {
        int[] bitSum = new int[32];
        for (int i = 0; i < arr.length; i++) {
            int bitMask = 1;
            for (int j = 31; j >= 0; j--) {
                int bit = arr[i] & bitMask;
                if (bit != 0) {
                    bitSum[j] += 1;
                }
                bitMask = bitMask << 1;
            }
        }
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = result << 1;
            result += bitSum[i] % 3;
        }
        return result;
    }
{% endhighlight %}

## 设计分数

分数题目做得中规中矩，但是实际面试当中能做到这个程度的大约10%，考虑到编程速度可以给个B+。toString写得很好，分子为0的判断其实我也没想到；构造函数通过抛出异常避免分母为0做得也很好，不过这个应该都能想到。

{% highlight java %}
public class Fraction {
    private int numerator;
    private int denominator;

    public Fraction(int numerator, int denominator) {
        if (denominator == 0) {
            throw new IllegalArgumentException("分母不能为0");
        }
        this.numerator = numerator;
        this.denominator = denominator;
    }

    public Fraction add(Fraction fraction) {
        int numerator = this.numerator * fraction.denominator + fraction.numerator * this.denominator;
        int denominator = this.denominator * fraction.denominator;
        return new Fraction(numerator, denominator);
    }

    public Fraction subtract(Fraction fraction) {
        int numerator = this.numerator * fraction.denominator - fraction.numerator * this.denominator;
        int denominator = this.denominator * fraction.denominator;
        return new Fraction(numerator, denominator);
    }

    public Fraction multiply(Fraction fraction) {
        int numerator = this.numerator * fraction.numerator;
        int denominator = this.denominator * fraction.denominator;
        return new Fraction(numerator, denominator);
    }

    public Fraction divide(Fraction fraction) {
        int numerator = this.numerator * fraction.denominator;
        int denominator = this.denominator * fraction.numerator;
        return new Fraction(numerator, denominator);
    }

    public Fraction simplify() {
        int gcd = gcd(this.numerator, this.denominator);
        return new Fraction(this.numerator / gcd, this.denominator / gcd);
    }

    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    @Override
    public String toString() {
        if (this.numerator == 0) {
            return "0";
        }
        if (this.denominator == 1) {
            return String.valueOf(this.numerator);
        }
        return this.numerator + "/" + this.denominator;
    }
}
{% endhighlight %}

分数题目当中，一个特殊的感受是chatgpt的题目能做多好，基本上和题目出的多好有很大关系。toString的时候本来只有简单的分子/分母形式，但是我增加了描述以后，就写得非常好。但是溢出情况上无论我怎么描述，它始终没有做任何处理，不知道为什么，溢出可以通过加减乘除的时候先约分一轮来缓解的。

## 时代变了，大人！

Chatgpt的两道题表现，我给A，通过。

面试Chatgpt的感受是，它的面试表现，其实取决于面试官的水平，面试官水平高，表达清楚，Chatgpt就做得好。它在谷歌拿了L3百万年薪，那么面试它的人水平应该不低。从这个角度来看，本文的这场面试，与其是说我在给Chatgpt出题，倒不如说是Chatgpt在给我出题。

当Chatgpt走进面试间……

如果它是候选人，那么这只是一场文字游戏而已；

如果它是面试官，那么意味着程序员面试的时代变了：可以让候选人来使用Chatgpt写程序，这需要候选人思路清晰、表达准确，Chatgpt才能写出正确的程序来，而且这个过程是高效、客观的。


将来，阿不，就是现在，可以考虑让Chatgpt走进面试间，至少代替面试的笔试部分，这也许是程序员面试的一种新形式。

[news]:https://www.infoq.cn/article/fxYffzDJGkdBofdUtsQH
