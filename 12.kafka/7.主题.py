import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("主题")
r2=s2.getRootTopic()
r2.setTitle("主题")


content={

'创建主题':[
    'kafka-topics.sh脚本的create指令，实际通过kafka.admin.TopicCommand类管理主题',
    'kafka-topics.sh脚本中的zookeeper、partitions、replication-factor(副本因子)和topic',
    {'实质':[
        '在ZooKeeper中的/brokers/topics节点下创建与该主题对应的子节点并写入分区副本分配方案',
        '在/config/topics/节点下创建与该主题对应的子节点并写入主题相关的配置信息'
    ]},
    '主题名称:由大小写字母、数字、点号“.”、连接线“-”、下画线“_”组成，不能只有点号“.”或双点号“..”',
    {'主题、分区、副本和Log之间的关系':[
        '主题和分区都是提供给上层用户的抽象，而在副本,Log层面才有实际物理上的存在',
        '同一个分区中的多个副本必须分布在不同的broker中，才能提供有效的数据冗余'
    ]}
],
'查看主题':[
    'kafka-topics.sh脚本中的list、describe指令',
],
'修改主题':[
    '由kafka-topics.sh脚本中的alter指令',
    '不支持减少分区'
],
'配置管理':[
    'kafka-configs.sh脚本:在运行状态下修改原有的配置，达到动态变更的目的'
],
'删除主题':[
    'kafka-topics.sh脚本中的delete指令,需broker端配置参数delete.topic.enable为true',
    '实质：在ZooKeeper中的/admin/delete_topics路径下创建一个与待删除主题同名的节点'
]


  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 