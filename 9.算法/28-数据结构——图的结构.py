import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("图的结构")
r2=s2.getRootTopic()
r2.setTitle("图的结构")


content={
'点的描述':[
    'class Node{',
    '   int value;',
    '   int in;',
    '   int out;',
    '   ArrayList<Node> nexts;',
    '   ArrayList<Edge> edges;',
    '                          ',
    '   Node(int value){',
    '   this.value=value;',
    '   in=0;',
    '   out=0;',
    '   nexts=new ArrayList<>();',
    '   edges=new ArrayList<>();',
    '}'
],
'边的描述':[
    'class Edge{',
    '   int weight;',
    '   Node from;',
    '   Node to;',
    '}',
],
'图的描述':[
    'class Graph{',
    '   HashMap<Integer,Node> nodes;',
    '   HashSet<Edge> edges;',
    '}',
],
'将别的数据结构转成上面的结构':[
    'Graph createGraph(Integer[][] matrix){'
    '   Graph graph=new Graph();',
    '   for(int i=0;i<matrix.length;i++){',
    '       Integer weight=matrix[i][0];',
    '       Integer from=matrix[i][1];',
    '       Integer to=matrix[i][2];',
    '       if(!graph.nodes.containKey(from)){',
    '           graph.nodes.put(from,new Node(from));',
    '       }',
    '       if(!graph.nodes.containKey(to)){',
    '           graph.nodes.put(to,new Node(to));',
    '       }',
    '       Node fromNode=graph.nodes.get(from);',
    '       Node toNode=graph.nodes.get(to);',
    '       Edge newEdge=new Edge(weight,fromNode,toNode);',
    '       fromNode.nexts.add(toNode);',
    '       fromNode.out++;',
    '       toNode.in++;',
    '       fromNode.edges.add(newEdge);',
    '       graph.edges.add(newEdge);',
    '   }',
    '   return graph;',
    '}'
]
}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 