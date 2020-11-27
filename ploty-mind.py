import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\ploty.xmind") 
s2=w.createSheet()
s2.setTitle("ploty")
r2=s2.getRootTopic()
r2.setTitle("ploty")


content={
'1.引入':[
    'from pyecharts.charts import *',
    'from pyecharts import options as opts',
    'from pyecharts.globals import ThemeType',
    'from pyecharts.components import Table'
],
'2.常用图':[
    '直方图:Bar()',
    '折线图:Line()',
    '箱形图:Boxplot()',
    '散点图:Scatter()'
],
'3.全局配置项':[
    {'InitOpts—初始化配置项':[
        'init_opts=opts.InitOpts()',
        "画布大小:width='600px', height='400px'",
        "主题配置:theme='dark'",
        "网页标题:page_title='AwesomeTang'",
        "背景颜色:bg_color='rgba(123, 200, 88, 0.4)'",
        
    ]},
    {'TitleOpts-标题配置项':[
        ".set_global_opts(title_opts=opts.TitleOpts())",
        "主/副标题:title='我是主标题', subtitle='我是副标题'",
        "标题位置:pos_left='center',pos_top='10%'",
        "标题样式"
    ]},
    {'LegendOpts-图例配置项':[
        '.set_global_opts(legend_opts=opts.LegendOpts())',
        "关闭/显示图例:is_show=True",
        "图例显示位置:pos_left='20%',pos_bottom='90%'",
        "图例水平/垂直布局:orient='vertical'",
        "图例形状:legend_icon='circle'"
    ]},
    {'TooltipOpts-提示框配置项':[
        ".set_global_opts(tooltip_opts=opts.TooltipOpts())",
        "触发设置:trigger_on='mousemove|click'",
        "提示框背景颜色: background_color='green'",
        ""
    ]},
    {'AxisOpts-坐标轴配置项':[
        ".set_global_opts(yaxis_opts=opts.AxisOpts())",
        "坐标轴名称:name='销售额/万元'",
        "坐标轴名称文本样式:name_textstyle_opts=opts.TextStyleOpts(color='red')",
        "坐标轴线—显示箭头:axisline_opts=opts.AxisLineOpts(is_show=True,symbol=['none', 'arrow'])",
        "坐标轴刻度-是否显示:  axistick_opts=opts.AxisTickOpts(is_show=False)",
        ''
    ]},
    'VisualMapOpts-视觉映射配置项',
    'DataZoomOpts-区域缩放配置项'
],
'4.系列配置项':[
    ".set_series_opts(itemstyle_opts=opts.ItemStyleOpts(color='green'))",
    ".add_yaxis('系列1', y_data_1,   itemstyle_opts=opts.ItemStyleOpts(color='green'))",
    {'ItemStyleOpts：图元样式配置项':[
        ".set_series_opts(itemstyle_opts=opts.ItemStyleOpts())",
        "颜色:color='green'",
        "透明度:opacity=0.5",
        "描边颜色:border_color='black'"
    ]},
    "TextStyleOpts：文字样式配置项",
    {'LabelOpts-标签配置项':[
        ".set_series_opts(label_opts=opts.LabelOpts())",
        "显示/关闭标签:is_show=False",
        "标签显示位置: position='inside'",
    ]},
    {'LineStyleOpts：线样式配置项':[
        ".add_yaxis('图例', y_data_1, linestyle_opts=opts.LineStyleOpts())",
        "线宽:width=5",
        "线型:type_='solid','dashed','dotted'",
        "线的颜色:color='black'"
    ]},
    {"SplitLineOpts-分割线配置项":[
        ".set_global_opts(xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts())",
        "显示X轴分割线:is_show=True"
    ]},
    {"SplitAreaOpts：分隔区域配置项":[
        ".set_global_opts(yaxis_opts=opts.AxisOpts(splitarea_opts=opts.SplitAreaOpts()",
        "显示Y轴分割区域:is_show=True,areastyle_opts=opts.AreaStyleOpts(opacity=1)"
    ]},
    'AreaStyleOpts：区域填充样式配置项',
    'EffectOpts-涟漪特效配置项',
    '标记点',
    '标记线',
    '标记区域'
],
'5.不常用':[
    '带涟漪效果散点图:EffectScatter()',
    '层叠图:overlap()',
    '地理坐标系:Geo()',
    '地图:Map()',
    '饼图:Pie()',
    '词云图:WordCloud()',
    '表格'
],
'学习来源':[
    'https://zhuanlan.zhihu.com/p/148748125',
    'https://www.kesci.com/mw/project/5eb7958f366f4d002d783d4a'
]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split("：")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t11 = t1.addSubTopic()
                t11.setTopicHyperlink(t1.getID()) 
                t11.setTitle(t)
                for j in i[t]:
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t111 = t11.addSubTopic()
                            t111.setTopicHyperlink(t11.getID()) 
                            t111.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t1111 = t111.addSubTopic()
                                        t1111.setTopicHyperlink(t111.getID()) 
                                        t1111.setTitle(n) 
                                        for l in m[n]:
                                            t11111 = t1111.addSubTopic()
                                            t11111.setTopicHyperlink(t111.getID()) 
                                            t11111.setTitle(l) 
                                else:
                                    t1111 = t111.addSubTopic()
                                    t1111.setTopicHyperlink(t111.getID()) 
                                    t1111.setTitle(m) 
                    else:
                        t111 = t11.addSubTopic()
                        t111.setTopicHyperlink(t11.getID()) 
                        t111.setTitle(j) 
        else:
            t11 = t1.addSubTopic()
            t11.setTopicHyperlink(t1.getID()) 
            t11.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\ploty.xmind") 