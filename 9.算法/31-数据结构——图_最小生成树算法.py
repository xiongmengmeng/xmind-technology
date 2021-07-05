import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("最小生成树算法")
r2=s2.getRootTopic()
r2.setTitle("最小生成树算法")


content={
'最小生成树算法之Kruskal':[
    '1.总是从权值最小的边开始考虑，依次考察权值依次变大的边',
    '2.当前的边要么进入最小生成树的集合，要么放弃',
    '3.如果当前的边进入最小生成树的集合中不会形成环，就要当前边',
    '4.如果当前的边进入最小生成树的集合中会形成环，就不要当前边',
    '5.考察完所有边之后，最小生成树的集合也得到了',
],
'代码':[    
    'Set<Edge> primMST(Graph graph){',
    '   PriorityQueue<Edge> priorityQueue=new PriorityQueue<>(',
    '           new EdgeComparator());'
    '   HashSet<Node> nodeset=new HashSet<>();',
    '   HashSet<Edge> edgeSet=new HashSet<>();',
    '   Set<Edge> result=new HashSet<>();', 
    '   for(Node node:graph.nodes.values()){',
    '       if(!nodeset.contains(node)){',
    '           nodeset.add(node);',
    '           for(Edge edge:node.edges){',
    '               if(!edgeSet.contains(edge)){',
    '                   edgeSet.add(edge);',
    '                   priorityQueue.add(edge);',
    '                }'
    '            }',
    '            while(!=priorityQueue.isEmpty()){',
    '                Edge edge=priorityQueue.poll();',
    '                Node toNode=edge.to;',
    '                if(!nodeset.contains(toNode)){',  
    '                   nodeset.add(toNode);',
    '                   result.add(edge);',
    '                   for(Edge nextEdge:toNode.edges){',
    '                       if(!edgeSet.contains(nextEdge)){',
    '                           edgeSet.add(nextEdge);',
    '                           priorityQueue.add(nextEdge);',
    '                       }' 
    '                   }',
    '               }',
    '           }',
    '       }'
    '       break;',
    '   }',
    '   return result;',
    '}'



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 