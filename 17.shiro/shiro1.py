import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="shiro"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("shiro")
r2=s2.getRootTopic()
r2.setTitle("shiro")


content={
'简介':[
    '一个强大易用的Java 安全框架',
    '认证、授权、加密、会话管理、与 Web 集成、缓存等'
],
'模块':[
    'Authentication：身份认证/登录，验证用户是不是拥有相应身份',
    'Authorization：授权/权限验证，验证某个已认证的用户是否拥有某个权限',
    'Session Manager：会话管理，即用户登录后就是一次会话，在没有退出之前，它的所有信息都在会话中',
    'Cryptography：加密，保护数据的安全性，如密码加密存储到数据库，而不是明文存储',
    'Web Support：Web支持，可以非常容易的集成到Web环境',
    'Caching：缓存，比如用户登录后，其用户信息、拥有的角色/权限不必每次去查，这样可以提高效率',
    'Concurrency：shiro支持多线程应用的并发验证，即如在一个线程中开启另一个线程，能把权限自动传播过去',
    'Testing：提供测试支持',
    'Run As：允许一个用户假装为另一个用户的身份进行访问',
    'Remember Me：记住我，常见的功能，即一次登录后，下次再来的话不用登录'
],
'组件':[
    {'Subject':[
        '主体，代表了当前 “用户”',
        '所有Subject都绑定到 SecurityManager，与Subject的所有交互都会委托给SecurityManager',
        'Subject认为是一个门面,SecurityManager才是实际的执行者'
    ]},
    {'SecurityManager':[
        '安全管理器',
        '所有与安全有关的操作都会与SecurityManager交互；且它管理着所有Subject',
        'Shiro的核心，它负责与后边介绍的其他组件进行交互，类springMvc中的DispatcherServlet'
    ]},
    {'Realm':[
        '域，Shiro 从Realm 获取安全数据（如用户、角色、权限）',
        '需要自己实现，类DataSource，即安全数据源'
    ]},
    {'Authenticator':[
        '认证器，负责主体认证的',
        '可扩展'
    ]},
    {'Authrizer':[
        '授权器，用来决定主体是否有权限进行相应的操作',
        '即控制着用户能访问应用中的哪些功能'
    ]},
    {'CacheManager':[
        '缓存控制器，来管理如用户、角色、权限等的缓存的',
        '因为这些数据基本上很少去改变，放到缓存中后可以提高访问的性能'
    ]},
    {'Cryptography':[
        '密码模块，Shiro提高了一些常见的加密组件用于如密码加密 / 解密的',
    ]}
],
'最简单的一个 Shiro 应用':[
    '1. 应用代码通过Subject进行认证和授权，而Subject又委托给SecurityManager',
    '2. 给Shiro的SecurityManager注入Realm，从而让SecurityManager能得到合法的用户及其权限进行判断',
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 