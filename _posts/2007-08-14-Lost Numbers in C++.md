---
layout: post
title: Lost Numbers in C++
date: 2007-08-14 20:00
categories: 编程
tags: C++
---
In C++, some numbers are lost, you will never be able to use them, display them or caculate them. Because they are lost! They can never exist in C++. Do you belive me?

Try this codes below please:

<!-- more -->

{% highlight cpp %}
     double a = 0.2;
{% endhighlight %}

Run it and set a break point after it, look at the value of a, what it is? Is it 0.2? No, it is 0.20000000000000001, in my computer. It may be other values such as 0.20000000000000002 or 0.19999999999999998, but it will never be 0.2. No matter what kinds of computer or what kinds of C++ compiler you are using.

The reason is simple, you can find it in the text book of   "Principle of computer", which is a very important course of computer science, but most of the programmers have forgetten it since the first time they konw it. The reason is that computer use binary digit system but we use decimal digit system and computer is limited.

As we all know, some fractions are finite decimals, such as 3/5, it is 0.6, but some are not, they are repeating infinite decimals, such as 1/3, it is 0.3333..., which is very familar with us when we are pupil. This is only the case in the world of decimal digit system, which is more familar with us. In the other digit systems, the reteating infinite decimals may be finite decimals, but finite decimals may become repeating infinite decimals. For example, in ternary digini system, 1/3 of decimals systme is not 0.333..., but it is 0.1 of ternary digini system. This is an example of repeating infinite decimals become finite decimals, but the example of finite decimlas changed to repeating infinite decimals is...

You are right! 1/5 in decimal digit system is repeating infinite decimals in binary system. 

Because another reason, computer is limited, so the infinite decimals can not be expressed actually in computer, and so does C++. So please take care when you use float numbers while programming, one of my colleagues was disturbed by this problem, and he spent a whole afternoon on it. This is the reason I write this article.

I have written a programme to show you the reason, but I haven't debugged it, you can try it. The propuse is to express a given number ( between 0 and 1, and open span) as power of 2. To compile it, you need to use C++ compiler of Visual C++ 2003, as I used __int64, which is a specific keyword of MS. To get the result, you need to imput two integer numbers first, then press Enter.

{% highlight cpp %}
#include <iostream>
int BinPower(unsigned __int64& m, unsigned __int64& n, unsigned __int64& binSum, int power);
int main()
{
 unsigned __int64 m, n, binSum;
 int p;
 std::cin >> m >> n;//input m, n
 binSum = 1;
 p = 0;
 std::cout << m << "/" << n << " = ";
 while(m < n && m != 0)
 {
   p = BinPower(m, n, binSum, p);
   std::cout << "+ 2 ^" << p << " ";
 }
 std::cout << "\n";
}
int BinPower(unsigned __int64& m, unsigned __int64& n, unsigned __int64& binSum, int power)
{
 if (m < n)
 {
   while(binSum * m < n)
   {
    binSum *= 2;
    --power;
   }
   m = binSum * m - n;
   n = binSum * n;
   unsigned __int64 r1 = m, m1 = m, n1 = n;
   while(r1 != 0)
   {
    r1 = n1 % m1;
    n1 = m1; 
    m1 = r1;
   }
   m = m / n1;
   n = n / n1;
  
   return power;
 }
 else
   return 1;
}

{% endhighlight %}
[原文在百度空间已经关闭]

