---
layout: post
title: XML and DTD
date: 2007-05-27 20:00
categories: 编程
tags: XML DTD
---
<!-- more -->
I used some XML in company, althought only very a little I used, but they are worth to be recorded. 

Reading and writing of XML As I know, there are two stand way for the reading and writing of XML: DOM and SAX. 

SAX will read the whole part of the XML file and yo can read from or write to the XML then. The advantage of SAX is that it is very easy to read or write the XML file; the disadvantage is that SAX has a bad efficiency, because it will read all the XML file before you can read or write the XML file. DOM will read the element of XML as a stream, the advantage of DOM is the good efficiency, but the disadvantage is that you will feel it hard to use. It's impossible to get easiness and effcieny in the same time, how wonderful it is if we can! So, just use SAX to read or write the small XML file; if the size of an XML file is larger that 1MB, it's better for you tu use DOM; but you are a real trouble maker if you insistant to use SAX when the size of XML file is more han 10 MB. The format of XMLThe format of XML is simple. One target of XML is to make a master of Computer Science can write a XML   parser in four weeks. Frankly speaking, I think a bachlar of Computer Science can do it, if he used regular expression, two weeks is enough (including one week of holiday).But it's not simple in other ways. A XML file which is able to read by the XML parser is only a well-formated XML file, it easy to write such a XML file: you only need to create a XML file by SAX using a correct XML parser (including the one created by a master of Computer Science in four weeks), then you must get a well-formated XML file. You have no chance to get wrong. But well-formated XML file is not always well-used XML file. For example, I design the formate of the XML file which will be used in our module, a Germany colleague will come to China and review our design next week. I thought it's too easy for me, and I can finish it in a short time. I did finish in a short time, but problems came soon. Because in other module, Germany offered a format of XML file, which is totally different from mine. Take the information of a book for example, I will write it like this:

<book index = "1"><name value = "Design Pattern"/><author value = "GOF"/></book>　　

But the Germany colleagues will write like this:

<book><name>Design Pattern</name><author>GOF</author></book>

I write all the data to the attribute of element in XML, but Germany colleague write most of the data to element. Then, who is correct? 

Clearly both of us are well-formated. It's a problem of how to use and define the tag. In my example, we should create an element with the tag of book, and then write author, book name and priece as attribute to the element. Neither of us gave a good formate, but I must admit that Germany colleagues's format is suitable for the file in our company, their format tells the logic relationship between data. XML file by me has a good looking only. If you have experience of Data Base, do you feels that to define and use the tag of XML looks quite like to deisgn a table in Data Base? To solve this problem, we need to introduce the last but not the least topic: DTD. Short introduction to DTDXML is quite familar with us, but DTD is known by little of us. At least I mistake it with TDD the first time I heard about it, so here is only short and simple introduction of DTD.  

DTD is short for Document Type Definition. It is used to make sure the XML file is correct, that is to say, we use DTD to make sure the tags, elements of XML file is written in the correct formate. For example above, one create each attribute as an element and then add attributes to the element, but another treat all the attributes as element. Who is right who is wrong? Both are right (well-formated), but if we continue to right without any change, the XML which is used to record the information of a book written by me can not be used by the Germany, and vice versa. Then XML loses its meaning. So we need to create a DTD file which tells us how to store the information to XML and how to get information from the XML, and the problem will be solved. Before reading a XML file, the parser can check the XML file by a DTD file to know whether the XML is in the format the parser wanted. There are a lot of product of intergation of DTD and XML, such as MathML, which defein a standard to describe the mathematics expressions by integating XML and DTD. These kinds of standard can not be born if DTD absent. Some mathematicians will write XML like this and some mathematician will write XML like that, just like what Newton and Leibnitz did with differential and integral calculus symbols. But the usage of DTD will not be much in the future, because there is some obvious default in DTD. First DTD is not follow the XML format, DTD   has its own grammer; second, DTD use ASCII as its character set, this is not a essential fault but it seems not so harmonious when XML uses unicode. There are some other faults, but I don't know ;-) 

So, a lot of new standard have been developed to take place of DTD or avoid to use DTD, such as XSLT, I remembered that in forum of CSDN, XSLT is used to format XML. But the most famous replacer is XML SChema, which has not fault of DTD but more powerful advantages.

[原文在百度空间已经关闭]

