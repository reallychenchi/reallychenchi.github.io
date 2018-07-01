---
layout: post
title: LocalPlacement浅析（一）
date: 2006-01-12 04:20
categories: 编程
tag: IFC
---
  IFCLOCALPLACEMENT在IFC中用于标记坐标系统，它由两部分组成：它所相对的坐标系统和它的原点、三个坐标轴方向。形式如下：
<!-- more -->
{% highlight python %}
#54=IFCLOCALPLACEMENT($,#20)
...
...
#95=IFCLOCALPLACEMENT(#54,#33)
#33=IFCAXIS2PLACEMENT3D(#94,#97,#96)
#94=IFCCARTESIANPOINT((0,5.500,0))
#97=IFCDIRECTION((1,0,0))
#96=IFCDIRECTION((0,0,1))
{% endhighlight %}

  其中，#54应该是另外一个IFCLOCALPLACEMENT，是#95所在的坐标系统相对的坐标系统。#33是一个IFCAXIS2PLACEMENT3D，它指明了原点和三个坐标轴的方向。而我们可以看到，#54也是一个LOCALPLACEMENT，但是它的第一个参数是省略的，用了$符号，这意味着#54是相对于原始坐标系统的(Golbal Coordinate)。

  IFCAXIS2PLACEMENT3D由三部分组成：原点、X轴的方向和Z轴的方向。在上例中，表示：#95坐标系统的原点是#54坐标系统的(0,5.500,0)点，X轴方向是#54坐标系统的(0,0,0)-(1,0,0)射线，Z轴方向是#54坐标系统的(0,0,0)-(0,0,1)射线。Y轴方向是根据XZ轴方向确定的。#95的XZ轴方向和#54的一样，也就是说，坐标轴方向不变。

IFCLOCALPLACEMENT is used to creat a coordinate system, it is composed by two part: The coordinate system it is related with and its origin point, the direction of its axis. For example:

{% highlight python %}
#54=IFCLOCALPLACEMENT($,#20)
...
...
#95=IFCLOCALPLACEMENT(#54,#33)
#33=IFCAXIS2PLACEMENT3D(#94,#97,#96)
#94=IFCCARTESIANPOINT((0,5.500,0))
#97=IFCDIRECTION((1,0,0))
#96=IFCDIRECTION((0,0,1))
{% endhighlight %}

In IFCLOCALPLACEMENT #95, #54 should be another IFCLOCALPLACEMENT, which #95 is relative with. #33 is an object of IFCAXIS2PLACEMENT3D, which special the origin point and direction of #95's axis. Notict that, #54 is also IFCLOCALPLACEMENT, but the first parameter is ommited, using $ instead, this means that #54 is relative with the golbal coordinate.IFCAXIS2PLACEMENT3D is composed of three parts: the origin poing, direction of X axis and direction of Z axis. In the sample above, #33 means that the origin point of #95 is the point (0, 5.500, 0) in #54, the direction of X axis is radial line (0, 0, 0)-(1, 0, 0) in #54, and the direction of X axis is radial line (0, 0, 0)-(0, 0, 1). The direction of Y axis is decided by directions of X axis and Z axis. The directions of X axis and Z axis in #95 is the same as #54, so #95 has the same axis direction of #54.

[原文来自我的教育网博客][原文来自我的教育网博客]

[原文来自我的教育网博客]:http://teacher.edu.cn/pc/article/200601/333805.html
