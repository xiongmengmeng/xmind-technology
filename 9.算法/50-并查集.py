import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("并查集")
r2=s2.getRootTopic()
r2.setTitle("并查集")


content={
'实现':[
    'class UnionSet<V>{',
    '   HashMap<V,Node<V>> nodes;',
    '   HashMap<Node<V>,Node<V>> parents;',
    '   HashMap<Node<V>,Integer> sizeMap;',
    '   UnionSet(List<V> values){',
    '       for(V value:values){',
    '           Node<V> node=new Node<>(value);',
    '           nodes.put(value,node);',
    '           parents.put(node,node);',
    '           sizeMap.put(node,1);',
    '   }'
    '}',
    'Node<V> findFather(Node<V> cur){',
    '   Stack<Node<V>> path=new Stack<>()',
    '   while(cur!=parents.get(cur)){',
    '       path.push(cur);',
    '       cur=parents.get(cur);',
    '   }',
    '   while(!path.isEmpty()){',
    '       parents.put(path.pop(),cur);',
    '   }',
    '   return cur;',
    '}',
    'boolean isSameSet(V a,V b){'
    '   if(!nodes.containKey(a)||nodes.containKey(b)){',
    '       return false',
    '   }'
    '   return findFather(nodes.get(a))==findFather(nodes.get(b));',
    '}',
    'void union(V a,V b){',
    '   if(!nodes.containKey(a)||nodes.containKey(b)){',
    '       return;',
    '   }',
    '   Node<V> aHead=findFather(nodes.get(a));',
    '   Node<V> bHead=findFather(nodes.get(b));',
    '   if(aHead!=bHead){',
    '       int aSetSize=sizeMap.get(aHead);',
    '       int bSetSize=sizeMap.get(bHead);',
    '       if(aSetSize>=bSetSize){',
    '           parents.put(bHead,aHead);',
    '           sizeMap.put(aHead,aSetSize+bSetSize);',
    '           sizeMap.remove(bHead);',
    '       }else{',
    '           parents.put(aHead,bHead);',
    '           sizeMap.put(bHead,aSetSize+bSetSize);',
    '           sizeMap.remove(aHead);',
    '       }',
    '   }',
    '}'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 