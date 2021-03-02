import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="shiro"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("身份验证")
r2=s2.getRootTopic()
r2.setTitle("身份验证")


content={
'AuthenticationToken':[
    'principals:身份,一般是用户名 / 密码 / 手机号',
    'credentials:证明,密码 / 数字证书',
],
'流程':[
    '1. 首先调用 Subject.login(token) 进行登录，其会自动委托给SecurityManager',
    '2. SecurityManager委托给 Authenticator 进行身份验证',
    '3. Authenticator：真正的身份验证者，Shiro API中核心的身份认证入口点，可以自定义插入自己的实现',
    '4. Authenticator委托给相应的AuthenticationStrategy进行多Realm身份验证',
    '5. Authenticator把相应的token传入Realm，从Realm获取身份验证信息' 
],
'SecurityManager':[
    {'SecurityManager接囗':[
        '继承Authenticator接囗',
        '方法：Subject login(Subject subject, AuthenticationToken authenticationToken)'
    ]},
    {'DefaultSecurityManager':[
        '实现SecurityManager接囗',
        {'重写方法login()':[
            '1.AuthenticationInfo info = authenticate(token);认证',
            '2.Subject loggedIn = createSubject(token, info, subject);创建Subject',
            '3.onSuccessfulLogin(token, info, loggedIn);Remember Me'
        ]}
    ]}
],
'Authenticator':[
     {'Authenticator接囗':[
        '方法：AuthenticationInfo authenticate(AuthenticationToken authenticationToken)',
    ]},
    {'ModularRealmAuthenticator类':[
        '实现Authenticator接囗',
        {'参数':[
            'Collection<Realm> realms',
            'AuthenticationStrategy authenticationStrategy：认证策略'
        ]},
        {'重写方法authenticate()':[
            '决定使用哪种策略执行认证realms'
        ]}
    ]}   
],
'Realm':[
    {'Realm接口':[
        'String getName():返回一个唯一的Realm名字',
        'boolean supports(AuthenticationToken token):判断此Realm是否支持此Token',
        'AuthenticationInfo getAuthenticationInfo(AuthenticationToken token):根据Token获取认证信息'
    ]},
    {'AuthorizingRealm':[
        '实现Realm接口',
        '重写getAuthenticationInfo(AuthenticationToken token)，调用模版方法doGetAuthenticationInfo(AuthenticationToken token)',
        'doGetAuthenticationInfo(AuthenticationToken token):鉴权，看账号密码对不对',
        '自定义实现一般继承它，并重写doGetAuthenticationInfo()方法'
    ]}  
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 