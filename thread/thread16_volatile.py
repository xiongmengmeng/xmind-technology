import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("volatile")
r2=s2.getRootTopic()
r2.setTitle("volatile")


content={

'volatile':[
    '强制从公共堆栈中取得变量的值，而不是从线程私有数据栈中取得变量的值',
    {'可见性':[
        {'lock前缀指令':[
            '借助了CPU的lock指令:使变量在多个线程间可见,不具有原子性',
            {'原则':[
                '写volatile时处理器会将缓存写回到主内存',
                '一个处理器的缓存写回到内存会导致其他处理器的缓存失效'
            ]},
            {'MESI':[
                '缓存一致性协议',
                'CPU写数据时，如发现操作变量是共享变量，发出信号通知其他CPU将该变量的缓存行置为无效',
                '当其他CPU需要读取变量时，发现缓存变量的缓存行无效，就会从内存重新读取',
                {'嗅探':[
                    '每个处理器通过嗅探在总线上传播的数据来检查自己缓存的值是否过期',
                    '当处理器发现自己缓存行对应的内存地址被修改，会将缓存行设置成无效',
                    '当处理器对数据进行修改时，会重新从系统内存中把数据读到处理器缓存中'
                ]},
                {'总线风暴':[
                    '由于MESI缓存一致性协议，需不断从主内存嗅探和cas不断循环',
                    '无效交互会导致总线带宽达到峰值'
                ]}
            ]}
        ]},
        {'内存屏障':[
            '内存屏障（memory barriers）：一组处理器指令，用于实现对内存操作的顺序限制',
            '读屏障:读取操作前加入读屏障，让工作内存中的数据失效，重新从主存读取到最新数据',
            '写屏障:写入数据后加入写屏障，让写入到工作内存中的数据更新到主内存，让其他线程可见',
        ]}

    ]},
    {'有序性':[
        {'禁止指令重排序':[
            {'指令重排':[
                '源代码 -> ',
                '编译器优化的重排 -> ',
                '指令并行的重排 ->',
                '指内存系统的重排 ->',
                '最终执行指令'
            ]},
            '多线程环境中线程交替执行，由于编译器优化重排->',
            '两线程中使用变量能否保证一致性无法确定，结果无法预测'
        ]},
        {'内存屏障':[
            '写屏障会确保指令重排序时，不会将写屏障之前的代码排在写屏障之后',
            '读屏障会确保指令重排序时，不会将读屏障之后的代码排在读屏障之前',
            '保证特定操作的顺序:禁止在内存屏障前后的指令执行重排序优化',
            '保证某些变量的内存可见性:刷新CPU缓存'
        ]}
    ]}

],
'synchronized和volatile比较':[
    '1.volatile:线程同步的轻量级实现，性能好，只能修饰变量',
    'synchronized:可修饰方法及代码块,使用面广',
    '2.多线程访问volatile不会发生阻塞，而synchronized会出现阻塞',
    '3.volatile:保证数据的可见性，不保证原子性',
    'synchronized:可保证原子性和可见性（会将私有内存和公共内存数据做同步）',
    '4.volatile解决变量在多个线程之间的可见性',
    'synchronized解决多线程之间访问资源的同步性'
]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 