## 5 设计模式

### 建议50：利用模块实现单例模式

单例是最常使用的模式，通过单例模式可以保证系统中一个类只有一个实例而且该实例易于被外界访问，从而方便对实例的个数控制，并节约系统资源。

Python单例模式：

    class Singleton(object):
        _instance = None
        def __new__(cls, *args, **kwargs):
            if not cls.instance:
                cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
            return cls._instance
    if __name__ == '__main__':
        s1 = Singleton()
        s2 = Singleton()
        assert id(s1) == id(s2) 

以上方法在并发的情况下可能发生意外，以下引入了带锁的版本：

    class Singleton(object):
        objs = {}
        objs_locker = threading.Lock()
        def __new__(cls, *args, **kv):
            if cls in cls.objs:
                return cls.objs[cls]
            cls.objs_locker.acquire()
            try:
                if cls in cls.objs:     # double check locking
                    return cls.objs[cls]
                cls.objs[cls] = object.__new__(cls)
            finally:
                cls.objs_locker.release()

利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现。但这个方案并不完美，至少还有以下两个问题：

> * 如果Singleton的子类重载了`__new__()`方法，会覆盖或者干扰Singleton类中`__new__()`的执行。
> * 如果子类有`__init__()`方法，那么每次实例化该Singleton的时候，`__init__()`都会被调用到，这显然是不应该的，`__init__()`只应该在创建实例的时候被调用一次。

有人开始重新审计Python的语法元素，发现模块采用的其实是天然的单例的实现方式：

> * 所有的变量都会绑定到模块；
> * 模块只初始化一次；
> * import机制是线程安全的（保证了在并发状态下模块也只有一个实例）

### 建议51：用mixin模式让程序更加灵活

与其他静态语言不同，Python语言中的基类在运行中可以动态改变。所以当我们向其中增加新的基类时，这个类就拥有了新的方法，也就是所谓的混入（minix）.

### 建议52：用发布订阅模式实现松耦合

发布订阅模式是一种编程模式，消息的发送者（发布者）不会发送其消息给特定的接受者（订阅者），而是将发布的消息分为不同的类别直接发布，并不关注订阅者是谁。而订阅者可以对一个或多个类别感兴趣，且只接收干兴趣的消息，并且不关注是哪个发布者发布的消息。

简单实现如下：

    from collections import defaultdict
    route_table = defaultdict(list)

    def sub(self, topic, callback):
        if callback in route_table[topic]:
            return
        route_table[topic].append(callback)
    def pub(self, topic, *a, **kw):
        for func in route_table[topic]:
            func(*a, **kw)

    import Broker
    def greeting(name):
        print 'Hello, %s.' % name
    Broker.sub('greet', greeting)
    Broker.pub('greet', 'Happyin3')
    # 输出
    Hello, Happyin3

相对于这个简化版本，blinker和python-message两个模块的实现要完备的多。blinker已经被用在了多个广受欢迎的项目上，比如flask和django；而python-message则支持更多丰富的特性。

### 建议53：用状态模式美化代码

所谓状态模式，就是当一个对象的内在状态改变时允许改变其行为，但这个对象看起来像是改变了棋类。状态模式主要用于控制一个对象状态的条件表达式过于复杂的情况，其可把状态的判断逻辑转移到表示不同状态的一系列类中，进而把复杂的判断逻辑简化。

举个例子：

    def workday():
        print 'work hard!'
    def weekend():
        print 'play harder'

    class People(object): pass

    people = People()
    while True:
        for i in xrange(1, 8):
            if i == 6:
                people.day = weekend
            if i == 1:
                people.day = workday
            people.day()

就这样，通过在不同的条件下将实例的方法（即行为）替换掉，就实现了状态模式。但是这个简单的例子仍然有以下缺陷：

* 查询对象的当前状态很麻烦；
* 状态切换时需要对原状态做一些清扫工作，而对新的状态需要做一些初始化工作，因为每个状态需要做的事情不同，去那不写在切换状态的代码中必然重复，所以需要一个机制来简化。

python-state包通过几个辅助函数和修饰函数很好的解决了这个问题，并且定义了一个简明状态机框架。
