import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据")
r2=s2.getRootTopic()
r2.setTitle("数据")


content={
'double':[
    '保留两位小数（double为浮点数)',
    '计算机存储为二进制类型，浮点类型转二进制会失精确度，因为二进制无法准确的表示0.1这类的值）',
],
'BigDecimal除以1000000，并四舍五入保留六位小数':[
    'BigDecimal result = originBulk.divide(new BigDecimal("1000000"),6,BigDecimal.ROUND_HALF_UP);',
    '/**',
    '* double类型数值保留小数',
    '* 常用roundingMode:',
    '*      BigDecimal.ROUND_HALF_UP-----四舍五入',
    '*      BigDecimal.ROUND_UP---向上取整',
    '*      BigDecimal.ROUND_DOWN---向下取整',
    '*/',
    'public static Double doublegetDecimal(Double origiNumber,Integer scale,Integer roundingMode) {',
    '    if (origiNumber == null) {',
    '        return 0.00;',
    '    }',
    '   //double转换成BigDecimal,推荐使用 BigDecimal.valueOf()',
    '   BigDecimal toBigDecimal = BigDecimal.valueOf(origiNumber).setScale(scale, roundingMode);',
    '   return toBigDecimal.doubleValue();',
    '}'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 