---
layout: post
title: CMake的交叉编译问题（Linux x86 - Linux arm11）
date: 2011-09-04 20:00
categories: 编程
tags: 
---

　　如果你的英文比较好，那么可以看这里：http://www.cmake.org/Wiki/CMake_Cross_Compiling，这是CMake官方网站上一篇介绍如何交叉编译的文章，我也是主要参考这篇文章完成了我的交叉编译。但是我的交叉编译过程不是翻译它的，是根据我自己交叉编译的过程，从了解CMake到完成交叉编译写的，容易入门，不涉及深入研究。

<!-- more -->



　　转载请注明原出处： http://hi.baidu.com/%E6%99%A8%E6%B1%A0/blog/item/c01992f9983b4e42252df227.html

概念性介绍

　　首先介绍一下CMake。本文是针对CMake菜鸟的，所以必须先对CMake有一个大概的认识，知道这是什么、怎么用以后，才可以考虑交叉编译不是？

　　CMake是一个跨平台自动编译工具，在KDE等开源项目当中有很好的应用，从而证明了CMake的强大功能。CMake的作用是根据设定的配置自动生成编译脚本，在Linux下就是生成Makefile，在Windows下就是生成VS的工程文件，这也是CMake产生的初衷和优点，使用CMake就可以为工程只写一个CMake脚本然后到各种平台上都能编译。比如一个跨平台的工程，可以在Linux、Windows和苹果上编译，那么以前的做法就是提供三套编译脚本，Linux下就是Makefile，Windows下就是VS的工程文件，如果有修改要添加删除文件呢，也只能三个地方都修改（任何一个程序员对会对这种做法嗤之以鼻，为什么不统一到一个地方呢？），而使用了CMake以后呢，就可以仅仅修改CMake的设定，然后运行CMake，CMake会根据当前的操作系统自动生成可用的的脚本，然后该Make就Make该VS就VS吧。

　　具体的使用呢，如果你拿到的是一个人家已经配置好的工程，那么一般来说敲cmake，就会发现目录下面多了一个Makefile出来，这时候敲make就可以编译通过了（顺利的情况下）。一般来说，会在Readme里面提示你，选用更合适的选项。如果要了解更多，请参考官方网站：http://www.cmake.org/cmake/help/cmake_tutorial.html





使用CMake

　　在对CMake有了概念上的认识和能简单的使用以后，我们就可以开始着手修改它来进行交叉编译了。首先要明确两个问题：CMake的大体工作流程是什么？它是根据什么脚本来生成对应平台的编译脚本呢？是这样的，在一个使用CMake编译的工程里，你都会发现CMakeList.txt这样一个文本，CMake开始执行的时候，都会从这个文件开始读取信息：要编译哪些文件、需要哪些库、在哪里找这些库、在哪里找对应的头文件、编译器是什么等等。也就是说，CMakeList.txt就是CMake的入口函数，要修改CMake就从CMakeList.txt开始。

　　打开CMakeList.txt以后，你会看到一堆用大写字母写的关键字堆出来的东西，不过没关系，咱们只是要修改它进行交叉编译，所以不用完全看懂（想完全看懂请参考上文链接，写的比我强多了），只要了解了关键的几个环节就可以了。必须知道的几个关键字是：

SET(<VARNAME> <VARVALUE>)

表示设置一个变量，比如SET(NUM 1)，设置NUM的值为1。中间用空格分开，不需要后面加分号。

MESSAGE("The value of Num is ${NUM}")

打印一条消息到屏幕，这对你调试很有帮助，如果要打印其中的变量，用${}引用。

FIND_PACKAGE(ZLIB REQUIRED)

查找一个库，库的名字是ZLIB，后面的REQUIRED是可选项，表示这个包是必须的，如果找不到不能生成Makefile。有了这句以后，一定有一个对应的FindZLIB.cmake，在这个文件里面，会有具体的如何查找ZLIB。





FIND_PATH(ZLIB_INCLUDE_DIR zlib.h “/home/release/arm11/include” NO_CMAKE_SYSTEM_PATH)

这句话应该出现在FindZLIB.cmake里面，表示在目录“/home/release/arm11/include”下查找文件zlib.h，找到以后，把路径放到变量ZLIB_INCLUDE_DIR里面。如果有多个目录，用空格或者换行分开放在后面就可以了，最好用引号引起来。



FIND_LIBRARY(ZLIB_LIBRARY_RELEASE NAMES ${ZLIB_LIBRARY_NAMES_RELEASE} 

    PATHS

    /home/release/vm_linux/arm11/zlib/lib

   /home/release/vm_linux/arm11/zlib/static_lib

  )





这句话也应该是出现在FindZLIB.cmake里面，表示在目录/home/release/vm_linux/arm11/zlib/lib和/home/release/vm_linux/arm11/zlib/static_lib里查找库文件，找到以后，把目录放在ZLIB_LIBRARY_RELEASE里面。注意，这里的库文件，没有像上面那样直接写出来，而是放在了变量ZLIB_LIBRARY_NAMES_RELEASE里面。也是完全可以直接写出来，用zlib就可以，这里不过就是提前用了SET语句，吧zlib设置到了ZLIB_LIBRARY_NAMES_RELEASE而已。需要注意的是，这里有个格式问题，必须把PATHS放在那里，跟在PATHS后面的目录，才会被查找到。

这也是一个多行书写和在多个目录里查找的例子。

 

开始交叉编译

　　交叉编译，比如Linux x86 到 Linux arm11，需要做的是：1、修改编译器，不能用x86的gcc了，要事先搭建好工具环境（这个在这里就不写了，网上大把）；2、把要交叉编译的工程所有依赖的库都统统替换成arm11编出来的，原来x86编译出来的不能用；3、一般来说，对应的头文件也需要换，当然理论上x86的头文件也可以用在arm11上，但是保险起见，还是用工具环境里面和库一起提供的头文件或者是你自己编库时候对应的头文件比较好。

　　设置交叉编译之前，必须在CMakeList.txt前面加上这样一句，这样CMake才会认为你是要交叉编译：

SET(CMAKE_SYSTEM_NAME Linux)

　　其中Linux是要编译过去的平台，如果你是在Linux下交叉编译Window的东西，就要写成Windows了。我是在Linux x86编Linux arm11，所以直接写Linux就可以了。

　　在通知CMake要交叉编译以后，还要告诉CMake到哪个路径下去找库文件，因为在交叉编译的时候CMake是不会自动去系统默认的目录找库文件和头文件的：



SET(CMAKE_FIND_ROOT_PATH "/home/release/arm11/library/gnuarm-4.4.2/")

SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)

SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)

SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

　　其中的第一行，是告诉CMake查找的根目录是什么。后面分别是告诉CMake怎么查找编译时候的工具程序的位置、库的位置和头文件的位置。设置为NEVER表示不查找，设置为ONLY表示只在CMAKE_FIND_ROOT_PATH设定的目录下查找，设置为BOTH（这是默认选项）表示既可以在系统目录下查找，也可以在CMAKE_FIND_ROOT_PATH下查找。因为咱们是交叉编译，所以后两项的设置了ONLY，对于编译时调用工具，一般来说是需要在系统目录下查找的，不过我不需要所以设置为NEVER。

　　然后，设置编译器：



SET(CMAKE_C_COMPILER "/usr/local/cross-tools/arm11/bin/linux-gnueabi-gcc")

　　直接把编译器的路径设置过去就可以了，CMAKE_C_COMPILER是C语言编译器，CMAKE_CXX_COMPILE是C++语言编译器。



　　设置完了这些以后，就要设置一下你的工程所依赖的库和头文件的位置了，这个很好办。先在CMakeList.txt里找FIND_PACKAGE提到的库，然后找这些库对应的FindXXX.cmake。一般来说，CMakeList.txt会通过INCLUDE引用FindXXX.cmake所在的目录的，如果实在没有线索，就用find -name *.cmake查找一把好了。

　　找到FindXXX.cmake以后，在FIND_PATH和FIND_LIBRARY里面的路径上添加上你需要的库的路径就可以了。我在上面写的，就是我自己进行arm11交叉编译的路径，原来的都是系统路径，比如/usr/include等。

　　完成以后，cmake -> make，就可以了。当然，不会一帆风顺，往往是你明明设置了路径，头文件和库文件分明在那里，可是它偏偏要么找不到，要么又找回了系统目录，那么这时候可以用MESSAGE打印一下，看看是不是没有执行到FIND_PATH和FIND_LIBRARY，也注意一下CMAKE_FIND_ROOT_PATH_MODE_LIBRARY和CMAKE_FIND_ROOT_PATH_MODE_INCLUDE的ONLY NEVER这些有没有设置正确。最危险的错误是，找到是找到了，但是找到的是系统目录下的库，这样CMake还是正常的，但是编译是不能通过的，这就需要你认真查看CMake的日志和多打印消息检查了。

OK，祝你在交叉编译的路上一路顺风！



 



[原文在百度空间已经关闭]

