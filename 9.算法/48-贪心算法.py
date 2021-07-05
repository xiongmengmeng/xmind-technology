import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("贪心算法")
r2=s2.getRootTopic()
r2.setTitle("贪心算法")


content={
'题2':[
    '给定一个字符串str,只由"X"和"."两种字符构成',
    '"X"表示墙，不能放灯，也不需要点亮',
    '""表示居民点，可以放灯，需要点亮',
    '如果灯放在i位置，可以让i-1,i和i+1三个位置被点亮,',
    '返回如果点亮str中所有需要点亮的位置，至少需要几盏灯',
    {'思路':[
        {'如果i位置为X':[
            '跳到i+1位置'
        ]},
        {'如果i位置为.':[
            '如i+1位置为"X",i位置放灯,跳到i+2位置',
            '如i+1位置为".",i+1位置放灯,跳到i+3位置'
        ]}
    ]},
    {'实现':[
        'int minLight(String road){',
        '   char[] str=road.toCharArray();',
        '   int index=0;',
        '   int light=0;',
        '   while(index<str.length){',
        '       if(str[index]=="X"){',
        '           index++;',
        '       }else{',
        '           light++;',
        '           if(index+1==str.length){',
        '               break;',
        '           }else{',
        '               if(str[index+1]=="X"){',
        '                   index=index+2;',
        '               }else{',
        '                   index=index+3;',
        '               }',
        '           }',
        '   }',
        '}',
        'return light;'
    ]}
],
'题3':[
    '一块金条切成两半，是需要花费和长度数值一样的铜板的，',
    '如长度为20的金条，不管怎么切，都要花费20个铜板，一群人想整块金条，怎么分最省',
    '输入一个数组，返回分割的最小代价',
    {'思路':[
        '将数组做堆排序',
        '从小到大来切割'
    ]},
    {'实现':[
        'int lessMoney(int[] arr){',
        '   PriorityQueue<Integer> pq=new PriorityQueue<>();',
        '   for(int i=0;i<arr.length;i++){',
        '       pq.add(arr[i]);',
        '   }',
        '   int sum=0;',
        '   int cur=0;',
        '   while(pq.size()>1){',
        '       cur=pq.poll()+pq.poll();',
        '       sum+=cur;',
        '       pq.add(cur);',
        '   }',
        '   return sum;'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 