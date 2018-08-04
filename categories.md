---
layout: page
permalink: /categories/
title: 分类/Categories
order: 1
---
<div id="archives">
    <h3 class="category-head">目录：</h3>
{% for category in site.categories %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <p class="category-head"><a href="#{{category_name}}">{{ category_name }}</a></p>
  </div>
{% endfor %}

    <h3 class="category-head">分类：</h3>
{% for category in site.categories %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <p></p>
    
    <h4 class="category-head">{{ category_name }}</h4>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
    <article class="archive-item">
      <h5><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h5>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>
