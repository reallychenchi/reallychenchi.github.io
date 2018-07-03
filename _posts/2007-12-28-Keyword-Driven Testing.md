---
layout: post
title: Keyword-Driven Testing
date: 2007-12-28 20:00
categories: 读书笔记
tags: 论文学习
---

Click the link below to visit the original webpage:

Keyword-Driven Testing

By Danny R. Faught
<!-- more -->

Summary: A curious phenomenon occurring among testers has caught Danny Faught's attention; testers everywhere are independently writing their own keyword-driven testing scripts. But what is keyword-driven testing, and how does it work? Is it better than data-driven testing? In this week's column, Danny reveals the testing method's simple design that has made it popular with many testers and non-testers alike.

I've noticed a curious phenomenon happening all over the place—testers are independently inventing keyword-driven testing. If so many testers are deciding it's a good idea, maybe it's worth a closer look. There are many other terms people have used to refer to the same general concept including "action words," "test frameworks," and "third-generation test automation." 

Here's an example of a keyword-driven test case:  

Action Fixture

start      fitnesse.fixtures.CountFixture       

check      counter      0

press      count       

check      counter      1

press      count       

check      counter      2

enter      counter      5

press      count       

check      counter      6

from URL http://fitnesse.org/FitNesse.ActionFixture

This looks too simple to be an automated test script, but too terse to be a manual test script. What's up? 

How Keyword-Based Testing Works 

You can use a keyword-based test for manual testing, but the technique really shines for automation. The process begins with a test designer writing a test case -- like the one above. The test designer doesn't have to know how to program; he could be a business analyst. A programming-savvy toolsmith implements a framework that provides keywords like "start," "check," "press," and "enter." The framework might make use of a separate interface driver, such as a graphical user interface (GUI) test tool. 

The wonderful thing about test scripts at this level of abstraction is that they can be independent of both the interface driver and the application's interface. Though the sample script above uses terms suggesting a GUI interface, the interface could be an application program interface (API), web service, or anything else. It's best to avoid embedding any assumptions about the design of the user interface in the keyword script. The framework can use an API early in the project, then later change to go through a GUI without modifying the test script. Testers can also change interface drivers without changing the script as long as the keyword framework isn't built into an interface driver. 

Have We Evolved? 

You may have heard of "data-driven testing," that uses a script roughly equivalent to the implementation of a single keyword. Along with the script, testers develop a list of data values that are fed to repeated invocations of the script. The difference between data-driven and keyword-driven testing is that each line of data in a keyword script includes a keyword that tells the framework what to do with the test data on that line. 



Some keyword framework designers like to write test cases that use multiple keywords, as in the example above, so the script looks like a simple programming language. Others prefer to have a single keyword that can perform the work of an entire test case, blurring the line between data-driven and keyword-driven testing. 



After reading the literature about these two approaches, I got the notion that keyword-driven testing is a more evolved version of data-driven testing. But I noticed that FitNesse users usually choose data-driven testing using the "column fixture" rather than keyword-driven testing using the "action fixture" as used in the example above. So maybe it's not as simple as one being a better version of the other. Though it's rarely done, you can use both at the same time by iterating a set of data values through multiple runs of a multi-line keyword script. 



The Right Reasons 

If you're not a programmer, you can still write automated tests if your organization supports keyword-driven test automation. I've talked to some people who have used keyword-driven testing who say that it's not practical to expect non-technical staff to write keyword scripts, but others have said it works fine. The jury is still out on that point. Managers need to understand that the team still needs programmers dedicated to implementing and maintaining the framework. 



The real benefit is the improved maintainability of the test scripts. The keyword approach follows in a longstanding tradition of modularizing the test automation so that it's easier to recover from user interface changes in the system under test. That benefit alone is sufficient to justify keyword-driven testing, even if all of the test designers are expert programmers. 



Thanks to Mike Silverstein, Mike Kelly, and Carl Nagle for their early feedback on this article. 



Further reading 

# "Keywords are the Key to Good Automation," presentation by Danny R. Faught. Includes a list of tools that support this technique, and additional synonyms and references.



# FitNesse at http://fitnesse.org/



# Just Enough Software Test Automation, Daniel J. Mosley and Bruce A. Posey, 2002



# Integrated Test Design and Automation, Hans Buwalda, Dennis Janssen, Iris Pinkster, 2002





About the Author

Danny R. Faught is a testing consultant, author, and trainer. Danny is the publisher of Open Testware Reviews and proprietor of Tejas Software Consulting based in Fort Worth, Texas. Visit tejasconsulting.com for more information.

[原文在百度空间已经关闭]

