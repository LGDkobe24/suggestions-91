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
