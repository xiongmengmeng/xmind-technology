import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="shiro"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Realm")
r2=s2.getRootTopic()
r2.setTitle("Realm")


content={
'自定义Realm':[
    '一般继承AuthorizingRealm',
    {'AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals)':[
        '鉴权',
        '内容：查询用户的所有权限信息',
        {'返回值AuthorizationInfo':[
            '作用：用于聚合授权信息',
            '方法：Collection<String> getStringPermissions() 获取权限字符串信息'
        ]}
    ]},
    {'AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token)':[
        '认证',
        '内容：判断用户跟密码是否正确',
        {'传参AuthenticationToken':[
            '收集用户提交的身份（如用户名）及凭据（如密码）',
            '自定义类实现该接囗'
        ]},
        {'返回值AuthenticationInfo':[
            {'作用':[
                '1.如果Realm是AuthenticatingRealm子类，可使用CredentialsMatcher进行凭据验证',
                '2.提供给SecurityManager来创建Subject（提供身份信息）'
            ]}
        ]}
    ]}
],
'Subject':[
    'Shiro 的核心对象，基本所有身份验证、授权都是通过Subject完成',
    'Subject自己不会实现相应的身份验证 / 授权逻辑',
    '通过DelegatingSubject委托给SecurityManager实现；可以理解为Subject是一个面门',
    {'使用':[
        'SecurityUtils.getSubject() 获取',
        '先查看当前线程是否绑定了Subject，如果没有通过Subject.Builder构建一个然后绑定到现场返回'
    ]},
    {'Subject一般使用场景':[
        '1. 身份验证（login）',
        '2. 授权（hasRole/isPermitted * 或 checkRole/checkPermission*）',
        '3. 退出'
    ]},
    {'方法':[
        {'1、身份信息获取':[
            'Object getPrincipal(); ',
            'PrincipalCollection getPrincipals(); '
        ]},
        {'2、身份验证':[
            'void login(AuthenticationToken token) ',
            'boolean isAuthenticated();',
            'boolean isRemembered();'
        ]},
        {'4、权限授权验证':[
            'boolean isPermitted(String permission);'
        ]},
        {'4.退出':[
            'void logout();'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 