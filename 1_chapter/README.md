## 引论

“罗马不是一天建成的”，编写代码水平的提升也不可能一蹴而就，同
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

* 占位符`%s`，数量多了以后，很难清楚哪一个占位符对应哪一个实
参。  
所以相对应的Pythonic代码是这样的：

    print 'Hello %(name)s!' % {'name': 'Tom'}

    value = {'greet': 'Hello world', 'language': 'Python'}
    print '%(greet)s from %(language)s.' % value

更具有Pythonic风格的代码：

    print '{greet} from {language}.'.format(
        greet = 'hellow world',
        language = 'Python')
