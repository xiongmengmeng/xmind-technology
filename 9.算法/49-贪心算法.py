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
'题4':[
    '输入：正数数组c,正数数组p,正数K,正数M',
    'c[i]表示i号项目的花费',
    'p[i]表示i号项目的扣除花费后的利润',
    'k表示能串行的最多做k个项目',
    'M表示初始资金',
    '备：每做完一个项目，马上获得的收益，可以支持你去做下一个项目，不能并行做项目',
    '输出：你最后获得的最大钱数',
    {'思路':[
        '根据花费将数组c构建成小根堆',
        '建一个大根堆，以利润为标准'
    ]},
    {'实现':[
        'class Program{',
        '   int p;',
        '   int c;',
        '}',
        'MinCostComparator implements Comparator<Program>{',
        '@Override',
        'public int compare(Program o1,Program o2){',
        '   return o1.c-o2.c;',
        '}',
        'MaxProfitComparator implements Comparator<Program>{',
        '@Override',
        'public int compare(Program o1,Program o2){',
        '   return o2.p-o1.p;',
        '}',
        'int findMaximizedCapital(int K,int K,int[] Profits,int[] Capital){',
        '   PriorityQueue<Program> minCostQ',
        '   =new PriorityQueue<Program>(new MinCostComparator());',
        '   PriorityQueue<Program> maxProfitQ',
        '   =new PriorityQueue<Program>(new MaxProfitComparator());',
        '   for(int i=0;i<Profits.length;i++){',
        '       minCostQ.add(new Program(Profits[i],Capital[i]));',
        '   }',
        '   for(int i=0;i<K;i++){',
        '       while(!minCostQ.isEmpty()&&minCostQ.peek().c<=W){',
        '           maxProfitQ.add(minCostQ.poll());',
        '       }',
        '       if(maxProfitQ.isEmpty()){',
        '           return W;',
        '       }',
        '       W+=maxProfitQ.poll().p;',
        '   }',
        '   return W;'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 