## 2 编程惯用法

### 建议8：利用assert语句来发现问题

断言（assert）在很多语言中都存在，它主要为调试程序服务，能够快速方便地检查程序的异常或者发行不恰当的输入等，可防止意想不到的情况出现。Python自1.5版本开始引入断言语句，其基本语法如下：  

    assert expression1 ["," expression2]

其中计算expression1的值会返回True或者False，当值位False的时候会引发AssertionErroe，而expression2是可选的，常用来传递具体的异常信息。

**对Python中使用断言需要说明如下：**

1. __debug__的值默认设置为True，且是只读的，在Python2.7中还无法修改该值。
2. 断言是有代价的，它会对性能产生一定的影响。对于编译型的语言，如C/C++，这也许并不那么重要，因为断言只在调试模式中启用。但Python并没有严格定义调试和发布模式之间的区别，通常禁用断言的方法是在运行脚本的时候加上`-O`标志，这种方式带来的影响是它并不优化字节码，而是忽略与断言相关的语句。  

**断言实际是被设计用来捕获用户所定义的约束的，而不是用来捕获程序本身错误的，因此使用断言需要注意一下几点：**

1. 不要滥用，这是使用断言的最基本的原则。
2. 如果Python本身的异常能够处理就不要再使用断言。
3. 不要使用断言来检查用户的输入。
4. 在函数调用后，当需要确认返回值是否合理是可以使用断言。
5. 当条件是业务逻辑继续下去的先决条件是可以使用断言。

### 建议9：数据交换值的时候不推荐使用中间变量

在Python中有更简单、更Pythonic的实现方式，代码如下：  

    >>> x, y = y, x

上面的实现方式不需要借助任何中间变量并且能够获取更好的性能。  

一般情况下Python表达式的计算顺序是从左到右，但遇到表达式赋值的时候表达式右边的操作数先于左边的操作数计算，因此表达式`expr3, expr4 = expr1, expr2`的计算顺序是`expr1, expr2 -> expr3, expr4`。因此对于表达式`x, y = y, x`，其在内存中执行的顺序如下：  

1. 先计算右边的表达式`y, x`，因此先在内存中创建元组`(y, x)`，其标示符和值分别为y、x及其对应的值，其中y和x是在初始化时已经存在于内存中的对象。
2. 计算表达式左边的值进行赋值，元组被一次分配给左边的标示符，通过解压缩，元组第一标识符（为y）分配给左边第一个元素（此时为x），元组第二个标识符（为x）分配给第二个元素（此时为y），从而达到x、y值交换的目的。

更深入一点我们从Python生成的字节码来分析。Python的字节码是一种类似汇编指令的中间语言，但是一个字节码指令并不是对应一个机器指令。我们通过dis模块来进行分析。

**dis自行查阅使用。**

### 建议10：充分利用Lazy evvaluation的特性

Lazy evaluation常被译为“延迟计算”或“惰性计算”，指的是仅仅在真正需要执行的时候才计算表达式的值。充分利用Lazy evaluation的特性带来的好处主要体现在一下两个方面：

1. **避免不必要的计算，带来性能上的提升。**
2. **节省空间，使得无限循环的数据结构成为可能。**

Lazy evaluation并不是一个很大、很新鲜的话题，但古人云“不积跬步无以至千里”，**小小的改进便能写出更为优化的代码**，何乐不为。

### 建议11：理解枚举替代实现的缺陷

在Python3.4以前并不提供枚举，于是人们充分利用Python的动态性这个特征，想出了枚举的各种替代实现方式。

1. 使用类属性。  

>     class Seasons:
          Spring = 0
          Summer = 1
          Autumn = 2
          Winter = 3

>     # 简化版本
      class Seasons:
          Spring, Summer, Autumn, Winter = range(4)

2. 借助函数。  

>     def enum(*posarg, **keysarg):
          return type("Enum", (object,), 
                      dict(zip(posarg, xrange(len(posarg))), **kwesarg))

>     Seasons = enum("Spring", "Summer", "Autumn", Winter=1)
      
3. 使用collections.namedtuple。  

>     Seasons = namedtuple('Seasons', 
                           'Spring Summer Autumn Winter')._make(range(4))

Python中枚举的替代实现方式还有很多，但是这些替代实现都有其不合理的地方。

> * 允许枚举值重复。
> * 支持无意义的操作。

Python2.7以后的版本还有另外一种替代选择——使用第三方模块`flufl.enum`，它包含两种枚举类：一种是Enum，只要保证枚举值唯一即可，对值的类型没有限制；还有一种是IntEnum，其枚举值为int型。

**Python3.4中根据PEP435的建议加入了枚举Enum，其实现主要参考了flufl.enum，但两者之间还是存在一些差别的。**

### 建议12：不推荐使用type来进行类型检查

作为动态性的强类型脚本语言，Python中的变量在定义的时候并不会指明具体类型，Python解释器会在运行时自动进行类型检查并根据需要进行隐式类型转换。按照Python的理念，**为了充分利用其动态性的特征是不推荐进行类型检查的。**  

如下面的函数`add()`，在无需对参数进行任何约束的情况下便可以轻松地实现字符串的连接、数字的加法、列表的合并等功能。

    def add(a, b):
        return a+b

    print add(1, 2j)            # 复数相加
    print add('a', 'b')         # 字符串连接
    print add(1, 2)             # 整数
    print add(1.0, 2.3)         # 浮点数处理
    print add([1, 2], [2, 3])   # 处理列表
    print add(1, 'a')           # 不同类型

不刻意进行类型检查，而是在出错的情况下通过抛出异常来进行处理，这是较为常见的方式。但实际应用中为了提高程序的健壮性，仍然会面临需要进行类型检查的情景。  

**内建函数`type(object)`用于返回当前对象的类型。**

但是，主张“不推荐使用type来进行变量类型检查”是有一定的缘由的。

> * 基于内建类型扩展的用户自定义类型，type函数并不能准确返回结果。
> * 在古典类中，所有类的实例的type值都相等。在古典类中，任意类的实例的type()返回结果都是`<type 'instance'>`。

因此对于内建的基本类型来说，也许使用type()进行类型的检查问题不大，但在某些特殊场合type()方法并不可靠。那么究竟应怎样来约束用户的输入类型从而使之与我们期望的类型一致呢？**答案是**：如果类型有对应的工厂函数，可以使用工厂函数对类型做相应转换，如`list(listing)`、`str(name)`等，否则可以使用`isinstance()`函数来检测。

### 建议13：尽量转换为浮点类型后再做除法

Python在最初的设计过程中借鉴了C语言的一些规则，比如选择C的long类型作为Python的整数类型，double作为浮点类型等。同时标准的算术运算，包括除法，返回值总是和操作数类型相同。作为静态类型语言，C语言中这一规则问题不大，因为变量都会预先申明类型，当类型不符的时候，编译器也会尽可能进行强制类型转换，否则编译会报错。但Python作为一门高级动态语言并没有类型申明这一说，因此在上面的例子中你不能提前申明返回的计算结果为浮点数，当除法运算中两个操作数都为整数的时候，其返回值也为整数，运算结果将直接截断，从而在实际应用中造成潜在的质的误差。

### 建议14：警惕eval()的安全漏洞

Python中eval()函数将字符串str当成有效的表达式来求值并返回计算结果。

“**eval is evil**”。

因此在实际应用过程中**如果使用对象不是信任源，应该尽量避免使用eval，在需要使用eval的地方可用安全性更好的ast.literal_eval替代**。

### 建议15：使用enumerate()获取序列迭代的索引和值

函数enumerate()是在Python2.3中引入的，主要是为了解决在循环中获取索引以及对应值的问题。它具有一定的惰性，每次仅在需要的时候才会产生一个(index, item)对。

enumerate()函数的内部实现非常简单，`enumerate(sqquence, start=0)`实际相当于如下代码：

    def enumerate(sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1

### 建议16：分清==与is的适用场景

is表示的是对象标示符，而==表示的意思是相等，显然两者不是一个东西。实际上，造成上面输出结果不一致的根本原因在于：is的作用是用来检查对象的标示符是否一致的，也就是比较两个对象在内存中是否拥有同一块内存空间，它并不适合用来判断两个字符串是否相等。`x is y`仅当x和y是同一个对象的时候才返回True，`x is y`基本相当于`id(x) == id(y)`。而==才是用来检验两个对象的值是否相等的，它实际调用内部`__eq__()`方法，因此`a == b`相当于`a.__eq__(b)`，所以==操作符是可以被重载的，而is不能被重载。

### 建议17：考虑兼容性，尽可能使用Unicode

Unicode(Universal Multiple-Octet Coded Character Set)，Unicode为每种语言设置了唯一的二进制编码表示方式，提供从数字代码到不同语言字符集之间的映射，从而可以满足跨平台、跨语言之间的文本处理要求。

Unicode的实现方式称为Unicode转换格式（Unicode Transformation Format），简称为UTF。

Python中处理中文字符经常会遇见的以下几个问题：

1.读出文件的内容显示为乱码。

> 分析：读入文件的编码和系统编码不一致，例如文件是以UTF-8编码保存的，Windows的本地默认编码是CP936，在Windows系统中它被映射为GBK编码，这两种编码不兼容。因此要解决这个问题可以使用Unicode作为中间介质来完成转换。首先需要对读入的字符用UTF-8进行解码，然后再用GBK进行编码。
>     (file.read().decode('utf-8')).encode('gbk')
> 其中，decode()方法将其他编码对应的字符串解码成Unicode，而encode()方法将Unicode编码转换为另一种编码，Unicode作为转换过程中的中间编码。
> **提醒**：上面的解决方法，在某些情况下（如文件是用Notepad软件以UTF-8编码形式保存）可能还会出现如下异常：
>     UnicodeEncodeError: 'gnk' codec can't encode character u'\ufeff' 
          in position 0: illegal multibyte sequence
>> 这是因为有些软件在保存UTF-8编码的时候，会在文件最开始的地方插入不可见的字符BOM（0xEF 0xBB 0xBF，即BOM）,这些不可见字符无法被正确的解析，而利用codecs模块可以方便地处理这种问题。
>>
>>     import codecs
    file = open("test.txt", 'r')
    content = file.read()
    file.close()
    if content[:3] == codecs.BOM_UTF8:    # 如果存在BOM字符则去掉
        content = content[3:]
    print content.decode('utf-8')

2.当Python源文件中包含中文字符的时候抛出SyntaxError异常。

> Python中默认的编码是ASCII编码（可以通过sys.getdefaultencoding()来验证），所以若文件是以ASCII形式保存的，并且字符串中包含中文字符。当调用print方法输出的时候会隐式地进行从ASCII到系统默认编码的转换，中文字符并不是ASCII字符，而此时源文件中又未制定其他编码方式，Python解释器并不知道如何正确处理这种情况，便会抛出异常。因此，要避免这种错误需要在源文件中进行编码声明，声明可用正则表达式`coding[:=]\s*([-\w.]+)`表示。

3.普通字符和Unicode进行字符串连接的时候抛出UnicodeDecodeError异常。

> 使用+ 操作符来进行字符串的连接时，+左边为中文字符串，类型为str，右边为Unicode字符串。当两种类型的字符串连接的时候，Python将左边的中文字符串转换为Unicode再与右边的Unicode字符串做连接。
> 解决上面的问题有以下两种思路：
>> * 指定str转为Unicode时的编码方式。
>> * 将Unicode字符串进行UTF-8编码。

