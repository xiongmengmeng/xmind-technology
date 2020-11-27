from pyecharts.charts import *
# from pyecharts.components import Table
from pyecharts import options as opts
# from pyecharts.commons.utils import JsCode
import random
# import datetime
from pyecharts.globals import ThemeType


#二.细节，各种配置学习

# 1.主题设置
# x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
# y_data_1 = [123, 153, 89, 107, 98, 23]
# y_data_2 = [231, 321, 135, 341, 245, 167]

# 所有内置主题
# theme_list = ['chalk',
#               'dark',
#               'essos',
#               'infographic',
#               'light',
#               'macarons',
#               'purple-passion',
#               'roma',
#               'romantic',
#               'shine',
#               'vintage',
#               'walden',
#               'westeros',
#               'white',
#               'wonderland']

# page = Page()
# for t in theme_list:

#     bar = (
#         Bar(init_opts=opts.InitOpts(
#             # 设置主题
#             theme=t))
#         .add_xaxis(x_data)
#         .add_yaxis('', y_data_1)
#         .add_yaxis('', y_data_2)
#         .set_global_opts(title_opts=opts.TitleOpts("Theme-{}".format(t)))
#     )
#     page.add(bar)

# page.render_notebook()


#2.配置项
#2.1全局配置项

# x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
# y_data_1 = [123, 153, 89, 107, 98, 23]
# y_data_2 = [231, 321, 135, 341, 245, 167]

# bar = (
#     Bar(init_opts=opts.InitOpts(width='600px', #图表画布宽度
#         height='400px',#图表画布高度
#         #图表主题  
#         theme='dark',
#         #网页标题 
#         page_title='AwesomeTang',
#         #图表背景颜色
#         bg_color='black',
#         #画图动画初始化配置
#         animation_opts=opts.AnimationOpts(animation_delay=1000, animation_easing="elasticOut"),
#         #渲染风格，可选 "canvas", "svg"
#         renderer='RenderType.CANVAS'))
#     .add_xaxis(x_data)
#     .add_yaxis('', y_data_1)
#     .add_yaxis('', y_data_2)
# )

# bar.render_notebook()

#2.2TitleOpts-标题配置项


x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 标题名称与位置 pos_top， pos_bottom，pos_left， pos_right分别对应 上/下/左/右
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis('', y_data_1)
    .add_yaxis('', y_data_2)
    .set_global_opts(title_opts=opts.TitleOpts(title="我是主标题",
        subtitle='我是副标题',
        pos_top='10%'))
)

bar.render_notebook()

#2.3LegendOpts-图例配置项

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis('图例1', y_data_1)
    .add_yaxis('图例2', y_data_2)
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=True,
        #图例位置
        pos_right='10%',
        pos_bottom='95%',
        #图例项的 icon'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
        legend_icon='circle'))
)
bar.render_notebook()


#2.4提示框配置

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]


bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis('图例1', y_data_1)
    .add_yaxis('图例2', y_data_2)
    .set_global_opts(tooltip_opts=opts.TooltipOpts(is_show=True,
        # 鼠标移动或者点击时触发
        trigger_on="mousemove|click",
        # 提示框背景颜色
        background_color="green"))
)

bar.render_notebook()


#2.5AxisOpts-坐标轴配置项
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 添加坐标轴名称
bar = (
    Bar(init_opts=opts.InitOpts(width='600px', #图表画布宽度
        height='400px',#图表画布高度
        #图表主题  
        theme='dark'))
    .add_xaxis(x_data)
    .add_yaxis('图例1', y_data_1)
    .add_yaxis('图例2', y_data_2)
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name='销售额/万元',
            min_=20, 
            max_=500,
            axisline_opts=opts.AxisLineOpts(is_show=True,symbol=['none', 'arrow'])),
        xaxis_opts=opts.AxisOpts(
            axisline_opts=opts.AxisLineOpts(is_show=True,symbol=['none', 'arrow']),
            axislabel_opts=opts.LabelOpts(
            color='gray',
            font_size=10,
            )))
)

bar.render_notebook()