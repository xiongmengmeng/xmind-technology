import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("矩阵")
r2=s2.getRootTopic()
r2.setTitle("矩阵")


content={
'转圈打印矩阵':[
    'int a=0;',
    'int b=0;',
    'int c=matrix.length-1;',
    'int d=matrix[0].length-1;',
    'boolean fromUp=false;',
    'while(a<=c&&b<=d){',
    '   printEdge(matrix,a++,b++,c--,d--);',
    '}',
    'void printEdge(int[][] m,int a,int b,int c,int d){',
    '   if(a==c){',
    '       for(int i=b;i<=d;i++){',
    '           System.out.print(m[a][i]+"");',
    '       }',
    '   }else if(b==d){',
    '       for(int i=a;i<=c;i++){',
    '           System.out.print(m[i][b]+"");',
    '       }',
    '   }else{',
    '       int curC=b;',
    '       int curR=a;',
    '       while(curC!=d){',
    '           System.out.print(m[a][curC]+"");',
    '           curC++;',
    '       }',
    '       while(curR!=c){',
    '           System.out.print(m[curR][d]+"");',
    '           curR++;',
    '       }',
    '       while(curC!=b){',
    '           System.out.print(m[c][curC]+"");',
    '           curC--;',
    '       }',
    '       while(curR!=a){',
    '           System.out.print(m[curR][b]+"");',
    '           curR--;',
    '       }',
    '   }',
    '}'
],



}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 