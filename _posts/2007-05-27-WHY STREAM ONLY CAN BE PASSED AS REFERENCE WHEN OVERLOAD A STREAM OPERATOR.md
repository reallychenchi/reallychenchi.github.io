---
layout: post
title: WHY STREAM ONLY CAN BE PASSED AS REFERENCE WHEN OVERLOAD A STREAM OPERATOR
date: 2007-05-27 20:00
categories: 编程
tags: C++
---


In C plus plus, stream opeator (>>) is offen overloaded, and we always overload it like this:

class CObj

<!-- more -->



{

     ...

};

std::ostream& operator << (std::ostream& strm, const CObj& objA)

{

     ...

     return strm;

}



When we pass stream as a parameter to a function, we will use reference, not value passed,Â Â  the main reason is that stream is a kind of resource, if we pass it as a valued passed parameter, the programme will copy the resource, and then the resource which is copied twice may be releaseed twice too, and this, may cause trouble. For the more, copying a stream also can cause two or more streams write to one file at same time. But this is only a reason in the logic, not a grammer rule, that is to say, we can pass stream as valued passed parameter, althought this is wrong:

class CObj

{

     ...

};

std::ostream operator << (std::ostream strm, const CObj& objA)

{

     ...

     return strm;

}

If we really write like this, the compiler (I use Visual C++ 7.0) will report a compile-time error, type mismatch or construcor not found (I can't remember the actual one). Why? Is it a grammer rule?

In fact, it is not a grammer rule that you can not pass stream as value when you overload the stream operator, in fact, it is a grammer rule that we MUST pass stream as reference or pointer (pointer is reference, for the compiler) when we want to pass stream as a parameter to a function. The reason is: In the structure of stream's class, no matter which stream it is, it only have one copy constructor without explicit which can accept a pointer of stream, that is to say, all the streams, do not have a copy constructor which can accept another stream as a value. This is the reason which cause an error if we pass a stream as a value.

If we pass a stream as a value to a function, the function will create a temporer vaiable, the temperor variable is created by a copy constructor which can accept a stream as value, but all the streams do not have such a copy sonsturcutor.

Compile-time error occur as a result! 

[原文在百度空间已经关闭]

