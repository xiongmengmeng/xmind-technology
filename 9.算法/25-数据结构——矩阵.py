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
'zigzag打印矩阵':[
    'int rR=0;',
    'int rC=0;',
    'int dR=0;',
    'int dC=0;',
    'int endR=matrix.length-1;',
    'int endC=matrix[0].length-1;',
    'boolean fromUp=false;',
    'while(tR!=endR+1){',
    '   printLevel(matrix,tR,tC,dR,dC,fromUp);',
    '   tR= tC=endC?tR+1:tR;',
    '   tC= tC=endC?tC+1:tC;',
    '   dC= dR=endR?dC+1:dC;',
    '   dR= dR=endR?dR:dR+1;',
    '   fromUp=!fromUp;',
    '}',
    'void printLevel(int[][] m,int tR,int tC,int dR,int dC,boolean f){',
    '   if(f){',
    '       while(tR!=dR+1){',
    '           System.out.print(m[tR++][tC++]+"");',
    '       }',
    '   }else{',
    '       while(dR!=tR+1){',
    '           System.out.print(m[dR++][dC++]+"");',
    '    }',
    '}'
],
'原地旋转正方形矩阵':[
    'int a=0;',
    'int b=0;',
    'int c=matrix.length-1;',
    'int d=matrix[0].length-1;',
    'boolean fromUp=false;',
    'while(a<c){',
    '   rotateEdge(matrix,a++,b++,c--,d--);',
    '}',
    'void rotateEdge(int[][] m,int a,int b,int c,int d){',
    '   int temp=0;',
    '   for(int i=0;i<d;i++){',
    '       temp=m[a][b+i];',
    '       m[a][b+i]=m[c-i][b];',
    '       m[c-i][b]=m[c][d-i];',
    '       m[c][d-i]=m[a+i][d];',
    '       m[a+i][d]=temp;',
    '    }',
    '}'
]



}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 