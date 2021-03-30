import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("B+树")
r2=s2.getRootTopic()
r2.setTitle("B+树")


content={
'B+树':[
    'https://www.jianshu.com/p/71700a464e97',
    '包含根节点、内部节点和叶子节点',
    '常用于数据库和操作系统的文件系统中',
    '数据稳定有序，插入与修改拥有较稳定的对数时间复杂度',
    '插入：当前结点key<=m-1，插入结束',
    '否则叶子结点分裂，左叶子结点含前m/2个记录，右结点含剩下的，第m/2+1个记录的key进位到父结点中',
    '删除: 结点的key>=Math.ceil(m/2)–1，删除结束',
    '否则若兄弟结点有富余，父结点key下移，兄弟结点key上移',
    '或当前结点和兄弟结点及父结点下移key合并成一个新的结点'
],
'B+树索引和hash索引的区别':[
    'hash索引底层 hash表,进行查找时,把键值换算成哈希值',
    'B+树底层 多路平衡查找树,查询从根节点出发,查找到叶子节点,同层级的节点间有指针相互链接，是有序的',
    'hash索引:等值查询更快,无法进行范围查询,不支持模糊查询'
],
'B树和B+树的区别':[
    'B树，每个节点都存储key和data，所有节点组成这棵树，并且叶子节点指针为null，叶子结点不包含任何关键字信息',
    'B+树，所有的叶子结点中包含了全部关键字的信息，及指向含有这些关键字记录的指针',
    '且叶子结点本身依关键字的大小自小而大的顺序链接',
    '所有的非终端结点可以看成是索引部分，结点中仅含有其子树根结点中最大（或最小）关键字'
],
'为什么要用 B-tree':[
    '散列表无法范围查找，也无法排序',
    '有序线性表更适合在内存，因为在磁盘插入不方便，也没有这么大的连续空间',
    'B+树可以范围查找，查询又快，而且叶子节点在磁盘中可以分开储存',
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 