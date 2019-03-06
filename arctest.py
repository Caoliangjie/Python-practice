import matplotlib.pyplot as plt
import numpy as np
def f(t):
    s1 = np.cos(2 * np.pi * t) ##这相当于在画曲线了
    e1 = np.exp(-t) ##exp就是指数函数e的x方
    return s1 * e1  #这就是画个曲线，具体什么样都可以看得到。
t1 = np.arange(0.0,5.0,.2) ##0-5的范围，0.2的间隔
l = plt.plot(t1,f(t1),'ro') ##用圆画出来,如果不加下面的艺术风格，就会画出很简单的红色圆点连成线
plt.setp(l, markersize=30)##相当于把点扩大30倍
plt.setp(l, markerfacecolor='C1')##后面这个facecolor应该是标注不同的颜色，改后面的id就可以看出来。
plt.show()
