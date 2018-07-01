# -*- coding:UTF-8 -*-
import re
import requests
from bs4 import BeautifulSoup

#First save the category page of year 2007 to file 2007.html, then run this script
f = open('2007.html', 'r')
for line in f.readlines():
    #http://teacher.edu.cn/pc/article/200606/333812.html
    mUrl = re.findall('http:\/\/teacher.edu.cn\/pc\/article\/\d+\/\d+\.html', line)
    for url in mUrl:
        print url
        req = requests.get(url)
        html = req.text
        bf = BeautifulSoup(html)
        author = bf.find_all('p', class_ = 'right article-rednum article-title-time')[0].text.encode('utf-8')
        #print author[0].text
        title = bf.find_all('div', class_ = 'article-title')[0].text.encode('utf-8')
        #print title[0].text
        texts = bf.find_all('div', class_ = 'article-body')[0].text.encode('utf-8')
        texts.replace("\n", "\n\n")
        #print texts[0].text

        date = author.split(' ')[0]
        fn = date + "-" + title+ ".md"
        postF = open(fn, 'w')
        postF.write("---\n")
        postF.write("layout: post\n")
        postF.write("title: " + title+ "\n")
        postF.write("date: " + author+ "\n")
        postF.write("categories: \n")
        postF.write("tag: \n")
        postF.write("---\n")
        postF.write("<!-- more -->\n")
        postF.write(texts+ "\n")
        postF.write("[原文来自我的教育网博客][原文来自我的教育网博客]\n\n")
        postF.write("[原文来自我的教育网博客]:" + url)
        postF.close()
