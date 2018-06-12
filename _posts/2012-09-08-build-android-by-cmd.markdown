---
layout: post
title:  "用命令行编译Android工程"
date:   2012-09-08 11:20:14 +0800
categories: jekyll update
---
　　今天终于做了我梦寐以求的一件事情就是用命令行编译成功了安卓工程。

　　安装ant，安装android开发环境，把android工具目录添加到路径当中，方便查找，这些就不一一细说，请自行搜索，版本使用最新的就可以。

　　安装完成以后，进入到Ecplise工程的目录下面，执行命令：

android update project -p e:prjprj_test

　　注意-p参数的意思是后面要跟上被更更新工程的目录，我的工程是放在e:prjprj_test下的。其实我当时是用了一个点，实在是博客这样写太容易误导了。　　

　　然后会生成build.xml和几个*.properites文件，这时候理论上就可以直接执行ant debug命令编译了，但是我还遇到这样几个困难：

　　首先，很多文件的编码不是UTF-8的，ant报告很多不认识的非法字符。这个最好就找个批量转换工具，都转换成UTF-8的好了，不然编码问题在编程中也会很麻烦，当然如果不能转换，就需要设置ant默认字符集为当前编程所用的字符集了——这个我没干过。

　　转换完成以后，ant又报告说某些文件前面有非法字符的，这个是因为windows上面，对于不同编码格式，有不同的头标记，如果用UE打开，转换到十六进制看这些被报错的文件，就会发现在正常的文字前面有EFBBBF两到三个字符，去除掉就可以了。如果文件多，那只有写个脚本了，如果文件少，直接用UE另存一下，但是注意格式要选择为UTF-8 No BOM。所谓的No BOM，就是指的不要那些头标记，在Windows上面，对于ansi、UTF-8和Unicode是有不同的头标记来区分的。

　　到了这一步还不算完，ant又报告说找不到一些定义的类型。我查找了一下，这些类型都是引用自某个jar库的，这样有两种办法解决，一个是在当前工程中创建一个libs目录，把你需要的jar文件都放进去；另外就是到default.properties添加一行指明要到哪里去找这些jar文件：

jar.libs.dir=../common/lib/

　　注意，我的例子前面有两个点表示上层目录，所有的jar都放在指定的目录里面。

　　到这里以后，用ant debug就可以生成apk文件了！

　　命令行编译的意义在于，这样就可以自动编译，自动签名自动发布了。关于给程序签名，可以参考http://developer.android.com/tools/publishing/app-signing.html ，这个说的很详细，照着做就可以了，没有上面那么多歪门邪道。

参考：

http://developer.android.com/tools/projects/projects-cmdline.html

http://stackoverflow.com/questions/3217643/how-to-add-external-jar-libraries-to-an-android-project-from-the-command-line

[教育网][教育网]

[教育网]:http://teacher.edu.cn/pc/article/201209/555761.html
