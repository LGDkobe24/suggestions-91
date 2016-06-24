## 4 库

### 建议36：掌握字符串的基本用法

无名氏说：编程有两件事，**一件是处理数值**，**另一件是处理字符串**。

* 利用Python遇到未闭合的小括号时会自动将多行代码拼接为一行和把相邻的两个字符串字面量拼接在一起的特性实现多行字符串的编写。

    >>> s = ('select * '
            'from atable '
            'where afield="value"')
    >>> s
    'select * from atable where afield="value"'

* 判断一个变量s是不是字符串应使用`isinstance(s, basestring)`，注意这里的参数是basestring而不是str。因为basestring才是str和unicode的基类，包含了普通字符串和unicode类型。

* 判定是否包含子串，推荐使用in和not in操作符。

### 建议37：按需选择sort()或者sorted()

Python中的排序相对简单，常用的函数有sort()和sorted()两种。

1. 相比于sort()，sorted()使用的范围更为广泛，两者的函数形式分别如下：  
    
    sorted(iterable[, cmp[, key[, reverse]]])
    s.sort([cmp[, key[, reverse]]])

> * cmp：为用户定义的任何比较函数
> * key：带一个参数的函数，用来为每个元素提取比较值。
> * reverse：表示排序结果是否反转。
   
   sorted()作用与任意可迭代的对象，而sort()一般作用于列表。

2. 当排序对象为列表的时候两者适合的场景不同。sorted(0函数会返回一个排序后的列表，原有列表保持不变；而sort()函数会直接修改原有列表，函数返回为None。

3. 无论是sort(0还是sorted()函数，传入参数key比传入参数cmp效率药膏。cmp传入的函数在整个排序过程会调用多次，函数开销较大；而key针对每个元素仅作一次处理，因此使用key比使用cmp效率药膏。

4. sorted()函数功能非常强大。

### 建议38：使用copy模块深拷贝对象

深拷贝和浅拷贝的概念：

* 浅拷贝：构造一个新的复合对象并将从原对象中发现的引用插入该对象中。浅拷贝的实现方式右多种，如工厂函数、切片操作、copy模块中的copy操作等。
* 深拷贝：也构造一个新的复合对象，但是遇到引用会继续地柜拷贝其所指向的具体内容，也就是说它会针对引用所指向的对象继续执行拷贝，因此产生的对象不受其他引用对象操作的影响。深拷贝的实现需要依赖copy模块的deepcopy()操作。

### 建议39：使用Counter进行计数统计

### 建议40：深入掌握ConfigParser

### 建议41：使用argparse处理命令行参数

docopt，它是比argparse更先进更易用的命令行参数处理器。但是目前还不是标准库。

### 建议42：使用pandas处理大型CSV文件

### 建议43：一般情况使用ElementTree解析XML

### 建议44：理解模块pickle优劣

### 建议45：序列化的另一个不错的选择——JSON

### 建议46：使用traceback获取栈信息

### 建议47：使用logging记录日志信息

### 建议48：使用threading模块编写多线程程序

### 建议49：使用Queue使多线程编程更安全


