## 引论

“罗马不是一天建成的”，编写代码水平的提升也不可能一蹴而就，通
过一点一滴的积累，才能达成从量变到质变的飞跃。

### 建议 1：理解Pythonic概念

    ＃ Python之禅

    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one -- obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

(3)**占位符`%s`**，数量多了以后，很难清楚哪一个占位符对应哪一个
实参。  
所以相对应的Pythonic代码是这样的：

    print 'Hello %(name)s!' % {'name': 'Tom'}

    value = {'greet': 'Hello world', 'language': 'Python'}
    print '%(greet)s from %(language)s.' % value

更具有Pythonic风格的代码：

    print '{greet} from {language}.'.format(
        greet = 'hellow world',
        language = 'Python')

### 建议2：编写Pythonic代码

1. 要避免劣化代码
> * 避免只用大小写来区分不同的对象。
> * 避免使用容易引起混淆的名称。
> * 不要害怕过长的变量名。

2. 深入认识Python有助于编写Pythonic代码
> * 全面掌握Python提供给我们的所有特性，包括语言特性和库特性。
> * 随着Python的版本更新、时间的推移，Python语言不断演进，社
区不断成长，还需要学习每个Python新版本提供的新特性，以及掌握
它的变化趋势。
> * 深入学习业界公认的比较Pythonic的代码，比如Flask、gevent和
requests.

3. 风格检查程序PEP8，有优秀的插件架构，可以方便地实现特定风格
的检测。类似的应用还有Pychecker、Pylint、Pyflakes等。其中，
Pychecker是Google Python Style Guide推荐的工具；Pylint因可以
非常方便地通过编辑配置文件实现公司或团队的风格检测而受到许多
人的青睐；Pyflakes则因为易于集成到vim中，所以使用的人也非常多。

**Pythonic的代码，往往是放弃自我风格的代码。**

### 建议3：理解Python与C语言的不同之处

3. 三元操作符“?:”
> `C ? X : Y`在Python中等价的形式位`X if C else Y`。

4. switch...case
> Python中没有C语言那样的`switch...case`分之语句。
> 可以用以下跳转来实现：
>>     def f(x):
           return {
               0: "You typed zero.\n",
               1: "You are in top.\n"
               }.get(n, "Only single-digit numbers are allowed")

**不要被其他语言的思维和习惯困扰，掌握Python的哲学和思维方式。**

### 建议4：在代码中适当添加注释

Python中有３中形式的代码注释：块注释、行注释以及文档注释。这
３种形式的惯用法大概有如下几种：　　

1. 使用块或者行注释的时候仅仅注释那些复杂的操作、算法，还有
可能别人难以理解的技巧或这不够一目了然的代码。

2. 注释和代码隔开一定的距离，同时块注释之后最好多留几行空白
再写代码。

3. 给外部可访问的函数和方法（无论是否简单）添加文档注释。注
释要清楚地描述方法的功能，并对参数、返回值以及可能发生的异常
进行说明，使得外部调用它的人员仅仅看docstring就能正确使用。

4. 推荐在文件头中包含copyright申明、模块描述等，如有必要，可
以考虑加入作者信息以及变更记录。

**有人说，写代码就像写诗，你见过谁在自己写的诗里加注释吗？**

### 建议5：通过适当添加空行是代码布局更为优雅、合理

1. 在一组代码表达完一个完整的思路之后，应该用空白行进行间隔。

2. 尽量保持上下文语义的易理解性。如当一个函数需要调用另一个函数的时候，尽量将它们放在一起，最好调用者在上，被调用者在下。

3. 避免过长的代码行，每行最好不要超过80个字符。

4. 不要为了保持水平对齐而使用多余的空格，其实使阅读者尽可能容易的理解代码所要表达的意义更重要。

5. 空格的使用要能够在需要强调的时候警示读者，在疏松关系的实体间起到分隔作用，而在具有紧密关系的时候不要使用空格。

### 建议6：编写函数的4个原则

函数能够带来最大化的代码重用和最小化的代码冗余。精心设计的函数不仅可以提高程序的健壮性，还可以增强可读性、减少维护成本。

> **原则１**　函数设计要尽量短小，嵌套层次不宜过深。
>
> **原则２**　函数申明应该做到合理、简单、易于使用。
>
> **原则３**　函数参数设计应该考虑向下兼容。
>
> **原则４**　一个函数只做一件事，尽量保证函数语句粒度的一致性。

**Python中函数设计的好习惯还包括：不要在函数中定义可变对象作为默认值，使用异常替换返回错误，保证通过单元测试等。**

### 建议7：将常量集中到一个文件

Python中使用常量一般来说右一下两种方式：

* 通过命名风格来提醒使用者该变量代表的意义位常量，如常量名所有字母大写，用下划线连接各个单词。

* 通过自定义的类实现常量功能。这要求符合“命名全部为大写”和“值一旦绑定便不可再修改”这两个条件。下面是一种较为常见的解决方法，它通过对常量对应的值进行修改时或者命名不符合规范时抛出异常来满足以上常量的两个条件。

>     class _const:
          class ConstError(TypeError): pass
          class ConstCaseError(ConstError): pass

          def __setattr__(self, name, value):
              if self.__dict__.has_key(name):
                  raise self.ConstError, "Can't change const.%s" % name
              if not name.isupper():
                  raise self.ConstCaseError, \
                        'const name "%s" is not all uppercase' % name
              self.__dict__[name] = value

      import sys
      sys.modules[__name__] = _const()

无论采用哪一种方式来实现常量，都提倡将常量集中到一个文件中，因为这样有利于维护，一旦需要修改常量的值，可以集中统一进行而不是逐个文件取检查。
