import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SpringBoot")
r2=s2.getRootTopic()
r2.setTitle("SpringBoot")



content={
'SpringBoot如何通过jar包启动':[
    {'使用':[
        'java -jar springbootstarterdemo-0.0.1-SNAPSHOT.jar)',
        'jar文件中包含的是class和资源文件'
    ]},
    {'MANIFEST.MF文件':[
        '记录了相关jar包的基础信息，包括入口程序',
        {'Start‐Class(应用自己的Main函数)':[
            'com.xxx.Application'
        ]},
        {'Main-Class(jar启动的Main函数)':[
            'org.springframework.boot.loader.JarLauncher'
        ]}
    ]},
],
'Jar包的打包插件及核心方法':[
    {'pom.xml':[
        '<build>',
        '   <plugins>',
        '   <plugin>',
        '       <groupId>org.springframework.boot</groupId>',
        '       <artifactId>spring‐boot‐maven‐plugin</artifactId>',
        '   </plugin>',
        '   </plugins>'
        '</build>'
    ]},
    {'maven clean package':[
        'spring‐learn‐0.0.1‐SNAPSHOT.jar.original'
    ]},
    {'总结':[
        {'JarLauncher':[
            '加载BOOT-INF/classes目录及BOOT-INF/lib目录下jar文件，实现了fat jar的启动'
        ]},
        {'SpringBoot':[
            '扩展JarFile、JarURLConnection及URLStreamHandler，实现了jar in jar中资源的加载'
        ]},
        {'SpringBoot':[
            '扩展URLClassLoader–LauncherURLClassLoader，实现了jar in jar中class文件的加载'
        ]},
        {'WarLauncher':[
            '加载WEB-INF/classes目录及WEB-INF/lib和WEB-INF/lib-provided目录下的jar文件',
            '实现war文件的直接启动及web容器中的启动'
        ]},
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 