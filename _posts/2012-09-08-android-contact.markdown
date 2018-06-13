---
layout: post
title:  "Android自带Contacts代码分析 1"
date:   2012-09-08 11:18:14 +0800
categories: jekyll update
---
Target: Find out the codes for search contacts and move it to the keyboard.

Based on the code of Android 2.3.7

1. When user press the search key in the Contacts, an search box will pop up for user, and "ldh" will get "Liu Dehua" or 刘德华. contacts_search_content.xml is the layout for searching contacts, it only used in ContactsListActivity.java.

2. Function ContactsListActivity.setupSearchView will set the change listener which will carry out searching task when user changed the characters

3. Find function ContactsListActivity.onSearchTextChanged

Comes to this function, nearly everything is in your hand.

Continue:

Now we know that the filter (such as "ldh") is set to mAdapter, then adapter will filter the correct result automatically. In fact the mAdapter is a CursorAdapter, it holds a cursor and the filter is set to the cursor. When the result get, function ContactItemListAdapter.changeCursor will be called.

Print the function call stack with changeCursor as below:

D/DBG ( 1899): com.android.contacts.ContactsListActivity.startQuery(ContactsListActivity.java:3346)

D/DBG ( 1899): com.android.contacts.ContactsListActivity.onResume(ContactsListActivity.java:1194)

D/DBG ( 1899): android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1150)

The first change is by onResume; and the rest changes are triggered by filter, in function onSearchTextChanged. Refer to codes .CursorFilter.publishResults for detail.

By now, the way how Android Contacts searches contacts is cleared, to get more detailed information, you have to look into the codes.

[原文来自我的教育网博客][原文来自我的教育网博客]

[原文来自我的教育网博客]:http://teacher.edu.cn/pc/article/201209/555758.html
