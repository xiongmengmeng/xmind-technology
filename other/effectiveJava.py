import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="effectiveJava"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("effectiveJava")
r2=s2.getRootTopic()
r2.setTitle("effectiveJava")



content={
'创建和销毁对象':[
    {'用静态工厂方法代替构造器':[
        '有名称',
        '不用每次调用都创建一个新的对象',
        '可以返回原返回类型的子类型对象',
        '通过静态方法的参数值，返回不同类的对象'
    ]},
    {'多构造器参数考虑使用Builder模式':[
        '可读性好'
    ]},
    '用私有构造器或枚举类型强化singleton属性',

    {'通过私有构造器强化不可实例化的能力':[
        '私有构造器内部抛AssertionError,防止类内部或反射调用',
        '构造器加注释说明 '
    ]},
    {'优先考虑依赖注入来引用资源':[
        '常见依赖注入框架：spring,dagger',
        '变体：将工厂传递给构造器，java8中增加的接囗Supplier<T>,最适合用于表示工厂'
    ]},
    {'避免创建不必要的对象':[
        '对于提供了静态工厂方法和构造器的不可变类：优先使用静态工厂方法',
        'Boolean.valueOf(String)优于Boolean(String)',
        '构造器每次调用都创建新的实例，而静态方法可以重用不可变的对象，也可以重用已知不会被修改的可变对象',
        '对于常量可以设置成static final的类型，让它成为类初始化的一部分，避免重复创建',
        '大量计算时优先使用基本数据类型，当心无意识的自动装箱'
    ]},
    {'消除过期的对象引用':[
        '如果类自己管理内存，应警惕内存泄漏问题：一旦元素被释放掉，元素中的任何对象引用都该被清空',
        '缓存，对弱引用WeakHashMap来引用缓存，可以保证缓存过期后被自动删除',
        '监听器和其它回调，也可以用WeakHashMap来引用回调'
    ]},
    '避免使用终结方法和清除方法',
    {'try-with-resources优先于try-finally':[
        '条件：当一个外部资源的句柄对象实现了AutoCloseable接口',
        '实现：将外部资源的句柄对象的创建放在try关键字后面的括号中',
        '结果：如果对外部资源的处理和对外部资源的关闭均遭遇了异常，“关闭异常”将被抑制，“处理异常”将被抛出',
        '“关闭异常”并没有丢失，而是存放在“处理异常”的被抑制的异常列表中'
    ]}
],
'对于所有对象都通用的方法':[
    {'覆盖equals时请遵守通用约定':[
        {'实现高质量equals方法的诀窍':[
            '使用==操作符楂“参数是否为这个对象的引用”',
            '使用instanceof操作符检查“参数是否为正确的类型”',
            '把参数转换成正确的类型',
            '对于该类中的每个“关键”域，检查参数中的域是否与该对象中对应的域相匹配'
        ]},
        {'注意':[
            '覆盖equals时总要覆盖hashCode',
            '不要将equals声明中的Object对象替换为其他类型'
        ]},
        {'自动生成':[
            '使用google开源的AutoValue框架',
            'IDE生成equals和hashCode方法',
            'lombok包中@Data'
        ]}
    ]},
    {'覆盖equals时总要覆盖hashCode':[
        '计算对象所有关键域的散列码，然后相加'
    ]},
    {'始终要覆盖toString':[
        '可以使用lombok包中@Data，自动生成toString方法'
    ]},
    {'谨慎覆盖clone':[
        '实现Cloneable接囗的类都应该覆盖clone()方法，返回类型为类本身',
        '方法内部先调用super.clone()方法，然后修正任何需要修正的域',
        '复制功能最好由构造器或工厂提供，复制数组最好用clone方法'
    ]},
    {'考虑实现Comparable接囗':[
        '当实现一个对排序敏感的类，都应该让其实现Comparable接囗,以便其实例被轻松分类与搜索',
        'compareTo方法中避免使用<和>操作符',
        '尽量使用包装类的静态compare方法',
        '或是在Comparator接囗中使用比较器构造方法'
    ]}],
'类和接囗':[
    '使类和成员的可访问性最小化',
    {'要在公有类而非公有域中使用访问方法':[
        '公有类永远都不应该暴露可变的域'
    ]},
    {'使可变性最小化':[
        '不可变对象本质是线程安全的，它们不要求同步',
        '缺点，对于每个不同的值都需要一个单独的对象',
        '很多不可变类，会有一个可变配套类，如String和StringBuffer'
    ]},
    {'复合优先于继承':[
        '与方法调用不同的是，继承打破了封装性',
        '扩展一个类时，改变原方法，可能原方法A调用了原方法B,在同时覆盖两方法时不知道这层逻辑，出错',
        '扩展一个类时，新增加一个方法A，可能新版本新增方法B与A同签名'
    ]},
    {'要么设计继承并提供文档说明 ，要么禁止继承':[
        '通过构造器调用私有的方法，final方法和静态方法是安全的，这些都不是可以被覆盖的方法'
    ]},
    {'接囗优于抽象类':[
        ''
    ]}

],
'':[

],
'':[

],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 