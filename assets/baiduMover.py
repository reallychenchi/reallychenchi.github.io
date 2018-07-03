# -*- coding:UTF-8 -*-
import re
import requests
import time
from bs4 import BeautifulSoup

def replace_invalid_filename_char(filename, replaced_char='_'):
    valid_filename = filename
    invalid_characaters = '\\/:*?"<>|'
    for c in invalid_characaters:
        valid_filename = valid_filename.replace(c, replaced_char)
    return valid_filename 

#Genrate the l.txt by list all wenzhang in static folder
f = open('l.txt', 'r')
for line in f.readlines():
    line = line.strip("\n")
    html = open(line, 'r')
    bf = BeautifulSoup(html)
    #author = bf.find_all('title')[0].text.encode('utf-8')
    #print author
    #content = bf.find(attrs={"name":"description"})['content'].encode('utf-8')
    #print content 
    title = bf.find('h1', class_ = 'pcs-article-title_ptkaiapt4bxy_baiduscarticle').text.encode('utf-8')
    print title
    content = bf.find('div', class_ = 'pcs-article-content_ptkaiapt4bxy_baiduscarticle').text.encode('utf-8')
    f = bf.find('div', class_ = 'pcs-article-content_ptkaiapt4bxy_baiduscarticle')
    f1 = f.find_all('p')
    print "\n\n"
    fileContent = ""
    do = 0
    count = 0
    for f0 in f1:
        #print f0.text.encode('utf-8')
        count = count + 1
        br = f0.find_all('br')
        if br:
            do = 2
            brstr = str(f0).replace("<br/>", "\n")
            count = count + 1
            brhtml = BeautifulSoup(brstr)
            #print brhtml.text
            fileContent = fileContent + "\n" + brhtml.text.encode('utf-8')
        else:
            do = 3
            fileContent = fileContent + "\n" + f0.text.encode('utf-8')
            #print f0.text.encode('utf-8')
    if count == 0:
        br = f.find_all('br')
        do = 4
        if br:
            do = 2
            brstr = str(f).replace("<br/>", "\n")
            count = count + 1
            brhtml = BeautifulSoup(brstr)
            fileContent = fileContent + "\n" + brhtml.text.encode('utf-8')
            #print brhtml.text
        """
        for linebreak in br:
            print "x"
            linebreak.extract()
        print f.prettify()
        """
    if count == 0:
        do = 1
        fileContent = fileContent + "\n" + f.text.encode('utf-8')
        #print f.text.encode('utf-8')
    print do, "***********\n"
    pos = fileContent.find("\n", 5)
    pos2 = 0
    if pos == -1:
        pos = 0
    if pos < 200:
        pos2 = fileContent.find("\n", pos + 3)
        if pos2 < 500 and pos2 > -1:
            print pos, pos2
            pos = pos2
    fileContent = fileContent[:pos] + "\n<!-- more -->\n" + fileContent[pos:]
    fileContent = fileContent.replace("\n", "\n\n")
    timeKey = bf.find('div', class_ = 'time-cang').text.encode('utf-8')
    dateStr = timeKey.replace("收藏于 ", "");
    postDate = dateStr + " 20:00"
    fn = replace_invalid_filename_char(dateStr + "-" + title+ ".md")
    postF = open("md/" + fn, 'w')
    postF.write("---\n")
    postF.write("layout: post\n")
    postF.write("title: " + title+ "\n")
    postF.write("date: " + postDate + "\n")
    postF.write("categories: 扯闲篇 编程\n")
    postF.write("tag: \n")
    postF.write("---\n")
    postF.write(fileContent + "\n\n")
    postF.write("[原文在百度空间已经关闭]\n\n")
    postF.close()
