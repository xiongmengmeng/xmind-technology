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
    '是以安全为目标的HTTP通道，简单讲是HTTP的安全版',
    '=HTTP+加密+认证+完整性保护',
    'HTTP： 直接通过明文在浏览器和服务器之间传递信息',
    'HTTPS： 采用 对称加密 和 非对称加密 结合的方式来保护浏览器和服务端之间的通信安全',
    '对称加密算法加密数据+非对称加密算法交换密钥+数字证书验证身份=安全'
],
'HTTPS加密请求（一次握手）过程':[
    '1.首先，客户端发起握手请求，以明文传输请求信息，包含版本信息，加密-套件候选列表，压缩算法候选列表，随机数，扩展字段等信息',
    '2.服务端的配置，采用HTTPS协议的服务器必须要有一套数字证书，可以自己制作，也可以向组织申请',
    '区别就是自己颁发的证书需要客户端验证通过，才可以继续访问，而使用受信任的公司申请的证书则不会弹出提示页面。这套证书其实就是一对公钥和私钥',
    '如果对公钥不太理解，可以想象成一把钥匙和一个锁头，只是世界上只有你一个人有这把钥匙，你可以把锁头给别人',
    '，别人可以用这个锁把重要的东西锁起来，然后发给你，因为只有你一个人有这把钥匙，所以只有你才能看到被这把锁锁起来的东西',
    '3.服务端返回协商的信息结果，包括选择使用的协议版本 version，选择的加密套件 cipher suite，选择的压缩算法 compression method、随机数 random_S 以及证书',
    '4.客户端验证证书的合法性，包括可信性，是否吊销，过期时间和域名'
    '(这部分工作是由客户端的SSL/TLS来完成的，首先会验证公钥是否有效，比如颁发机构，过期时间等等',
    '，如果发现异常，则会弹出一个警示框，提示证书存在的问题。如果证书没有问题，那么就生成一个随机值',
    '然后用证书（也就是公钥）对这个随机值进行加密。就好像上面说的，把随机值用锁头锁起来，这样除非有钥匙，不然看不到被锁住的内容。)
    '5.客户端使用公匙对对称密匙加密，发送给服务端',
    '这部分传送的是用证书加密后的随机值，目的是让服务端得到这个随机值，以后客户端和服务端的通信就可以通过这个随机值来进行加密解密了',
    '6.服务器用私钥解密，拿到对称加密的密匙',
    '(服务端用私钥解密后，得到了客户端传过来的随机值',
    '然后把内容通过该随机值进行对称加密，将信息和私钥通过某种算法混合在一起',
    '这样除非知道私钥，不然无法获取内容，而正好客户端和服务端都知道这个私钥，所以只要加密算法够彪悍，私钥够复杂，数据就够安全。)
    '7.传输加密后的信息，这部分信息就是服务端用私钥加密后的信息，可以在客户端用随机值解密还原。
    '8.客户端解密信息，客户端用之前生产的私钥解密服务端传过来的信息，于是获取了解密后的内容。整个过程第三方即使监听到了数据，也束手无策

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'
],
'RT':[
    'Response-time:响应时间',
    '执行一个请求从开始到最后收到响应数据所花费的总体时间',
    '即从客户端发起请求到收到服务器响应结果的时间'
],
'Concurrency':[
    '并发数:系统同时能处理的请求数量，反应系统的负载能力'
],
'吞吐量':[
    '系统的承压能力',
    '和处理对CPU的消耗、外部接口、IO等因素紧密关联',
    '单个处理请求对CPU消耗越高，外部系统接口、IO速度越慢，系统吞吐能力越低，反之越高',
    {'系统吞吐量有几个重要指标参数':[
        'QPS（TPS）',
        '并发数',
        '响应时间'
    ]}
],
'关系':[
    'QPS（TPS）= 并发数/平均响应时间',
    '并发数 = QPS*平均响应时间'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 