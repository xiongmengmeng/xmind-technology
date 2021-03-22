import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("拷贝过程对比")
r2=s2.getRootTopic()
r2.setTitle("拷贝过程对比")


content={
'中断方式':[
    '1.用户进程发起数据读取请求',
    '2.系统调度为该进程分配cpu',
    '3.cpu向io控制器(ide,scsi)发送io请求',
    '4.用户进程等待io完成，让出cpu',
    '5.系统调度cpu执行其他任务',
    '6.数据写入至io控制器的缓冲寄存器',
    '7.缓冲寄存器满了向cpu发出中断信号',
    '8.cpu读取数据至内存',
    {'缺点':[
        '中断次数取决于缓冲寄存器的大小'
    ]}
],
'DMA 技术':[
    '1.用户进程发起数据读取请求',
    '2.系统调度为该进程分配cpu',
    '3.cpu向DMA发送io请求',
    '4.用户进程等待io完成，让出cpu',
    '5.系统调度cpu执行其他任务',
    '6.数据写入至io控制器的缓冲寄存器',
    '7.DMA不断获取缓冲寄存器中的数据（需要cpu时钟）',
    '8.传输至内存（需要cpu时钟）',
    '9.所需的全部数据获取完毕后向cpu发出中断信号',
    {'优点':[
        '减少cpu中断次数，不用cpu拷贝数据'
    ]}
],
'学习':[
    'https://blog.csdn.net/weixin_42096901/article/details/103017044',
    'https://blog.csdn.net/lzb348110175/article/details/100853071'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 