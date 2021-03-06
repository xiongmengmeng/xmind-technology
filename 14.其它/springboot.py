import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet() 
s2.setTitle("springboot")
r2=s2.getRootTopic()
r2.setTitle("springboot")

# Create a topic with a link to the first sheet given by s2.getID()
line=['IOC','AOP']

content={
'IOC':[
    'Bean装配',
    '依赖注入',
    {'Bean的生命周期':[
        'Bean定义:资源定位并将Bean的定义发布到IoC容器',
        'Bean的初始化:Bean的实例化和依赖注入',
        'Bean的生存期',
        'Bean的销毁']},
    'Bean的作用域',
    'Profile'],
'AOP':[
    '连接点（join point）',
    '切点（point cut）',
    '通知（advice）',
    '目标对象（target）',
    '引入（introduction）',
    {'织入（weaving）':['通过动态代理技术，为原有服务对象生成代理对象','拦截与切点匹配的连接点','按约定将各类通知织入约定流程']},
    '切面（aspect）',
    '数据库连接',
    {'事务':['@Transactional','事务定义器 TransactionDefinition','事务管理器 PlatormTransactionManager','@Transactional调用失效问题']}],
'Datasource':[
    '配置数据源:可以使用tomcat自带的，也可以使用第三方数据源',
    'JdbcTemplate',
    'JPA',
    {'MyBatis':['Configuration','SqlSessionFactory','Interceptor']}],
'整合redis':[
    '5种基本数据类型',
    '存储：RDB,AOF',
    '事务',
    '管道',
    'LUA脚本',
    {'RedisTemplate':['opsForXXX()','boundXXXOps()','execute():SessionCallback和RedisCallback']}],
'整合mongodb':[
    '@Document @id @Field',
    'MongoTemplate'],
"springmvc":[
    {'DispatcherServlet':[
        '1.HTTP Request',
        '2.HandlerMapping:处理器映射，定位控制器方法',
        '3.HandlerExecutionChain:处理器执行链，包含处理器和拦截器',
        '4.HandlerAdapter',
        '5.ModelAndView']},
    {'Web服务器启动,初始化一些组件':['HandlerMapping','HandlerAdapter']},
    {"用户发起请求后":[
        '1.通过HandlerMapper机制就能找到对应的控制器.封装成HandlerExecutionChain对象',
        '2.HandlerExecutionChain对象包含一个处理器（handler）和拦截器数组',
        '3.适配器HandlerAdapter去运行处理器handler',
        '4.得到数据，Model'
    ]},
    {'处理器映射HandlerMapper':[
        '启动阶段会将注解@RequestMapping所配置的内容保存到处理器映射（HandlerMapping）',
        '请求的到来，通过拦截请求信息与HandlerMapping进行匹配，找到对应的处理器（它包含控制器的逻辑）',
        '将处理器及其拦截器保存到HandlerExecutionChain对象']},
    {'获取控制器参数':[
        '无注解下获取参数',
        '使用@RequestParam获取参数',
        '传递数组',
        '传递JSON：方法的参数标注为@RequestBody',
        '通过URL传递参数',
        '获取格式化参数',
        '自定义参数转换规则:一对一转换器（Converter）']},
    '数据模型',
    {'视图':['逻辑视图:会使用视图解析器（ViewResolver）','非逻辑视图：PDF,EXCEL,JSON']},
    {'拦截器':['继承HandlerInterceptor','通过WebMvcConfigurer注册拦截器']}],
'整合shiro':[
    {'自定义Realm，继承AuthorizingRealm ':['获取身份验证信息','授权信息']},
    {'身份验证:doGetAuthenticationInfo(AuthenticationToken token)':[
        '1.获取用户信息',
        '2.封装好SimpleAuthenticationInfo',
        '3.交给AuthenticatingRealm使用CredentialsMatcher进行密码匹配']},
    {'授权信息:doGetAuthorizationInfo(PrincipalCollection principals)':[
    '1.获取用户信息',
    '2.将用户的角色和权限赋值到authorizationInfo',
    '3.交给AuthenticatingRealm使用CredentialsMatcher进行密码匹配']},
    {'密码加密':['散列算法','散列次数','随机字符串作为salt因子,生成salt']},
    {'ShiroConfig':[
        'realm初始化时，注入CredentialsMatcher',
        'DefaultWebSecurityManager在初始化时,注入realm',
        'ShiroFilterFactoryBean初始化，注入过滤器和SecurityManager','']}
]

}



#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
