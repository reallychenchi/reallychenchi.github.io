---
layout: post
title: Three steps of improvement of a function
date: 2008-07-18 20:00
categories: 编程
tags: C++
---


Here are the three steps, the instructions will be added later on.

1. 

<!-- more -->

{% highlight cpp %}
int extract_subsegment(void *io_data_buf)
{
     int l_err;
     s_if *l_if_ptr;
     int l_idx;
     int i;
     s_subsegment l_subsgement;
     s_file_handle l_handle;
     
     l_err = file_open(&l_handle);
     while(FE_SUCCESS == l_err)
     {
        l_idx = 0;
        while(l_idx < l_if_ptr->ip_addr_count)
        {
           for(i = 0; i < COUNT_C; ++i)
              l_subsegment[i] = l_subsegment[i] | l_if_ptr->subsegment[i];
           l_idx = l_idx + 1;
        }           
        
        l_err = file_read(&l_handle, l_if_ptr);             
     }
     file_close(&l_handle);
     l_err = extract_subsegment(io_data_buf, l_subnet);
     free(io_data_buf);
     
     return l_err;  
}  

2. 
int extract_subsegment(void *io_data_buf)
{
     int l_err;
     s_if *l_if_ptr;
     int l_idx;
     int i;
     s_subsegment l_subsgement;
     s_file_handle l_handle;
     
     l_err = file_open(&l_handle);
     while(FE_SUCCESS == l_err)
     {
        l_idx = 0;
        while(l_idx < l_if_ptr->ip_addr_count)
        {
           for(i = 0; i < COUNT_C; ++i)
              l_subsegment[i] = l_subsegment[i] | l_if_ptr->subsegment[i];
           l_idx = l_idx + 1;
        }           
        
        l_err = file_read(&l_handle, l_if_ptr);             
     }
     if (FE_NOT_FOUND != l_err)
     {
        file_close(&l_handle);
        free(io_data_buf);
        return l_err;
     }
     file_close(&l_handle);
     l_err = extract_subsegment(io_data_buf, l_subnet);
     free(io_data_buf);
     
     return l_err;  
}

3.
int extract_subsegment(void *io_data_buf)
{
     int l_err;
     s_if *l_if_ptr;
     int l_idx;
     int i;
     s_subsegment l_subsgement;
     s_file_handle l_handle;
     
     l_err = file_open(&l_handle);
     while(FE_SUCCESS == l_err)
     {
        l_idx = 0;
        while(l_idx < l_if_ptr->ip_addr_count)
        {
           for(i = 0; i < COUNT_C; ++i)
              l_subsegment[i] = l_subsegment[i] | l_if_ptr->subsegment[i];
           l_idx = l_idx + 1;
        }           
        
        l_err = file_read(&l_handle, l_if_ptr);             
     }
     if (FE_NOT_FOUND == l_err)
     {
        l_err = extract_subsegment(io_data_buf, l_subnet);
     }
     file_close(&l_handle);
     free(io_data_buf);
     
     return l_err;  
}
{% endhighlight %}
[原文在百度空间已经关闭]

