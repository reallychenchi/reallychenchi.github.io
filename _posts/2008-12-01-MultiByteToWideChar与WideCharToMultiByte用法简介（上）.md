---
layout: post
title: MultiByteToWideChar与WideCharToMultiByte用法简介（上）
date: 2008-12-01 20:00
categories: 编程
tags: C++ MFC
---

　　这里简单介绍一下如何使用MultiByteToWideChar与WideCharToMultiByte。利用这两个函数可以实现对任意的编码类型的转换，具体说来，就是MultiByteToWideChar可以把任何编码类型转换成Unicode，然后WideCharToMultiByte可以把Unicode转换成其他编码。

<!-- more -->



MultiByteToWideChar：

　　作用是把其他编码形式转换成Unicode，有六个参数：

　　1、UINT类型，要转换的编码类型代码，GBK的代码是936，其他编码的代码如果用得着请去MSDN查；

　　2、字符类型设置，如果你拿不准，就用MB_PRECOMPOSED | MB_USEGLYPHCHARS；

　　3、一个LPCSTR类型指针，指向要转换的字符串，可以直接用char *强制转换；

　　4、要转换的字符串的长度，如果是-1，那么函数认为这是一个用0x0结尾的字符串，但是注意，在这种情况下，函数也会在转换以后的Unicode字符串中增加一个0x0，请根据你的需要保留与否（要去掉，注意Unicode占用两个字节，所以要删除两个char大小；

　　5、一个LPCWSTR类型指针，指向一个用来保存生成的Unicode字符串的空间，必需足够大；

　　6、LPCWSTR指向空间的大小，如果这个值为0，那么函数不进行任何转换，而是返回所需要的大小，注意此处的大小，是以Unicode字符计算的，也就是两个char一个单位。

　　返回值为0说明调用失败，否则成功：在第六个参数为零的时候，返回实际需要的Unicode字符数；在第六个参数不为零的时候，返回实际写入的Unicode字符数。

　　在使用中，按照上述要求设置参数就可以了。其中，第六个参数，可以调用两次MultiByteToWideChar函数来实现，第一次调用时候，把第六个参数设置为0，通过返回者获得实际需要的大小，第二次调用再设置进去；简单一点，直接就设置大小为要转换字符串大小两倍就可以，肯定够用。当然，这里设置多大空间，那么第五个参数那里就一定要申请到，否则内存管理失败的程序很失败。

　　示范代码如下：
{% highlight cpp %}
#include "windows.h"
#include <vector>
/*
GBKstrm    The stream for GBK characters
Ustrm    The stream for unicode charachters
returns  
    0 success
    -1 Unknown error
    -2 ... -6 Internal error, not enough buffer, for internal errors, 
       bug must exists in these functions, refer to MSDN for
       MultiByteToWideChar & WideCharToMultiByte
*/
int GBKToUnicode(std::istream& GBKstrm, std::ostream& Ustrm)
{
//GBKstrm must good
//UTFstrm must good
//GBKstrm must be a stream for GBK characters
int result;
LPCSTR pstr = NULL;
LPWSTR pwbuf = NULL;
int size;
//Read GBK to gbkBuf first
std::vector<char> gbkBuf;
while (GBKstrm.good())
{
    char buf;
    GBKstrm.read(&buf, 1);
    gbkBuf.push_back(buf);
}
gbkBuf.push_back(0);//Terminated by NULL
pstr = (LPCSTR)&gbkBuf[0];//pstr point to gbkBuf
size = (int)gbkBuf.size() * 2 + 2;//TODO: Here the size can be smaller
pwbuf = (LPWSTR)malloc(size * sizeof(WCHAR));
result = MultiByteToWideChar(936,//The code page of GBK
    MB_PRECOMPOSED | MB_USEGLYPHCHARS,
    pstr,//string for convert
    -1,//The string is terminated with NULL character
    pwbuf,//buffer for UTF
    size);//size of buffer;
if (result == 0)//function fail
{
    switch (GetLastError())
    {
    case ERROR_INSUFFICIENT_BUFFER:
     return -2;
     break;
    case ERROR_INVALID_FLAGS:
     return -3;
     break;
    case ERROR_INVALID_PARAMETER:
     return -4;
     break;
    case ERROR_NO_UNICODE_TRANSLATION:
     return -5;
     break;
    default:
     return -1;
    }
}
else
{
    Ustrm.write((char *)pwbuf, result * (sizeof(WCHAR) / sizeof(char)) - 1);//Remove the NULL character
    if (Ustrm.good())
     return 0;
    else
     return -6;
}
free(pwbuf);
}
{% endhighlight %}

[原文在百度空间已经关闭]

