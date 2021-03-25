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
'客户端和服务端之间的加密机制':[
    '1.TCP的握手过程',
    {'2.TLS的握手':[
        'client1：TLS版本号+所支持加密套件列表+希望使用的TLS选项'',
        'Server1:选择一个客户端的加密套件+自己的公钥+自己的证书+希望使用的TLS选项+（要求客户端证书）',
        'Client2:(自己的证书)+使用服务器公钥和协商的加密套件加密一个对称秘钥（自己生成的一个随机值）',
        'Server2:使用私钥解密出对称秘钥（随机值）后，发送加密的Finish消息，表明完成握手'
    ]}
    '注：非对称加密算法非常耗时，而对称加密快很多',
],
'数字签名':[
    {'数字签名的制作过程':[
        'CA拥有非对称加密的私钥和公钥',
        'CA对证书明文信息进行hash',
        '对hash后的值用私钥加密，得到数字签名',
    ]},
    '明文和数字签名共同组成了数字证书，这样一份数字证书就可以颁发给网站了',
    {'浏览器验证过程':[
        '1.拿到证书，得到明文T，数字签名S',
        '2.用CA机构的公钥对S解密（由于是浏览器信任的机构，所以浏览器保有它的公钥），得到S’',
        '3.用证书里说明的hash算法对明文T进行hash得到T’',
        '4.比较S’是否等于T’，等于则表明证书可信'
    ]}
],
'学习':[
    'https://zhuanlan.zhihu.com/p/43789231'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 