import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="shiro"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("授权")
r2=s2.getRootTopic()
r2.setTitle("授权")


content={
'基本概念':[
    '授权，也叫访问控制，即在应用中控制谁能访问哪些资源',
    {'几个关键对象':[
        {'主体（Subject）':[
            '访问应用的用户，在Shiro中使用Subject代表该用户'
        ]},
        '资源（Resource）',
        {'权限（Permission）':[
            '资源：：操作,表示用户能不能访问某个资源',
        ]},
        '角色（Role）'
    ]},
    '授权方式:可使用注解',
],
'流程':[
    '1.调用Subject.isPermitted接口',
    '2.其会委托给SecurityManager',
    '3.SecurityManager接着委托给Authorizer',
    '4.Authorizer:真正的授权者，如调用如 isPermitted(“user:view”)，其首先会通过PermissionResolver把字符串转换成Permission实例',
    '5.在进行授权前，调用相应的Realm获取Subject相应的权限用于匹配传入的权限',
    '6.Authorizer判断Realm的权限是否和传入的匹配',
    '如有多个Realm，会委托给ModularRealmAuthorizer进行循环判断，如果匹配如 isPermitted*会返回true，否则返回false表示授权失败'
],
'Subject':[
    {'Subject接囗':[
        'boolean isPermitted(String permission)',
        'boolean hasRole(String roleIdentifier);'
    ]},
    {'DelegatingSubject':[
        '实现Subject接囗',
        '重写isPermitted(String permission)：',
        '调用securityManager.isPermitted(getPrincipals(), permission)'
    ]},
],
'SecurityManager':[
    {'SecurityManager接囗':[
        '继承Authorizer接囗',
    ]},
    {'AuthorizingSecurityManager.':[
        '实现SecurityManager接囗',
        {'重写方法isPermitted()':[
            'this.authorizer.isPermitted()'
        ]}
    ]}
],
'Authorizer':[
     {'Authorizer接囗':[
        '方法：boolean isPermitted(PrincipalCollection principals, String permission);',
    ]},
    {'ModularRealmAuthorizer':[
        '实现Authorizer接囗',
        {'参数':[
            'Collection<Realm> realms;',
            'PermissionResolver permissionResolver：解析权限字符串到Permission实例'
        ]},
        {'重写方法isPermitted()':[
            '遍历Realm，执行其isPermitted方法'
        ]}
    ]}   
],
'Realm':[
    {'AuthorizingRealm':[
        '重写isPermitted(PrincipalCollection principals, String permission)',
        '1.AuthorizationInfo info = getAuthorizationInfo(principals);获得用户所有权限信息',
        '调用模版方法doGetAuthorizationInfo(AuthenticationToken token)',
        '2.isPermitted(permission, info):判断是否有权限',
        '自定义实现一般继承它,重写getAuthorizationInfo()方法'
    ]}  
],
'权限注解':[
    '引入AuthorizationAttributeSourceAdvisor，其本质是一个Advisor，利用SpringAop实现代理',
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 