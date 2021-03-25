import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HTTPS")
r2=s2.getRootTopic()
r2.setTitle("HTTPS")


content={
'HTTPS':[
    'Hypertext Transfer Protocol Secure，超文本传输安全协议',
    '是以安全为目标的HTTP通道，即HTTP的安全版',
    '=HTTP+加密+认证+完整性保护',
    {'对比':[
        'HTTP：直接通过明文在浏览器和服务器之间传递信息',
        'HTTPS：采用【对称加密】和【非对称加密】结合的方式来保护浏览器和服务端间的通信安全',
    ]},
    '数字证书验证身份+非对称加密算法交换密钥+对称加密算法加密数据=安全'
],
'HTTPS加密请求（一次握手）过程':[
    {'1.客户端发起握手请求':[
        '以明文传输请求信息',
        '包含版本信息，加密-套件候选列表，压缩算法候选列表，随机数，扩展字段等信息',
    ]},
    {'2.服务端配置':[
        '采用HTTPS协议的服务器必须要有一套数字证书，可自己制作，也可向组织申请',
        '区别:自己颁发的证书需客户端验证通过，才可以继续访问，受信任的公司申请的证书不会弹出提示页面',
        '这套证书其实就是一对公钥和私钥',
        {'对公私钥':[
            '可想象成一把钥匙和一个锁头',
            '世界上只有你有这把钥匙，你可以把锁头给别人',
            '别人用这个锁把重要的东西锁起来，然后发给你，因只有你有这把钥匙，所以只有你才能看到被这把锁锁起来的东西'
        ]}
    ]},
    {'3.服务端返回协商的信息结果':[
        '包括选择使用的协议版本version，选择的加密套件cipher suite，选择的压缩算法compression method',
        '随机数random_S及证书'
    ]},
    {'4.客户端验证证书合法性':[
        '包括可信性，是否吊销，过期时间和域名',
        {'验证工作由客户端的SSL/TLS完成':[
            '验证公钥是否有效，比如颁发机构，过期时间等等',
            '如发现异常，弹出一个警示框，提示证书存在的问题',
            '如证书没问题，生成一个随机值',
            '用证书（即公钥）对这个随机值进行加密'
        ]}
    ]},
    {'5.客户端使用公匙对【对称密匙】加密，发送给服务端':[
    ]},
    {'6.服务器用私钥解密，拿到【对称加密的密匙】':[
        '服务端用私钥解密后，得到了客户端传过来的随机值（对称密匙）',
        '把内容通过该【对称密匙】进行对称加密',
    ]},
    {'7.传输加密后的信息':[
        '信息就服务端用【对称密匙】加密后的信息，可以在客户端用【对称密匙】解密还原',
    ]},
    {'8.客户端解密信息':[
        '客户端用【对称密匙】解密服务端传过来的信息，获取了解密后的内容',
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 