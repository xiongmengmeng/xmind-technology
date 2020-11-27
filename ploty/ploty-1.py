from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import random
import datetime
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

#一.ploty能画的图

#直方图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]
bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
      )

bar.render_notebook()


#折线图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]
line = (Line()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
      )

line.render_notebook()


#箱形图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [[random.randint(100, 200) for i in range(10)] for item in x_data]

Box = Boxplot()
Box.add_xaxis(x_data)
Box.add_yaxis("", Box.prepare_data(y_data))
Box.render_notebook()


#散点图
# x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
# y_data = [123, 153, 89, 107, 98, 23]

# scatter = (Scatter()
#            .add_xaxis(x_data)
#            .add_yaxis('', y_data)
#            )

# scatter.render_notebook()

#带涟漪效果散点图
# x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
# y_data = [123, 153, 89, 107, 98, 23]

# effectScatter = (EffectScatter()
#            .add_xaxis(x_data)
#            .add_yaxis('', y_data)
#            )

# effectScatter.render_notebook()

#层叠图

# x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
# y_data_bar = [123, 153, 89, 107, 98, 23]
# y_data_line = [153, 107, 23, 89, 123, 107]


# bar = (Bar()
#        .add_xaxis(x_data)
#        .add_yaxis('', y_data_bar)
#        )

# line = (Line()
#         .add_xaxis(x_data)
#         .add_yaxis('', y_data_line)
#         )

# overlap = bar.overlap(line)
# overlap.render_notebook()


#GEO-地理坐标系
# province = [
#     '广东',
#     '湖北',
#     '湖南',
#     '四川',
#     '重庆',
#     '黑龙江',
#     '浙江',
#     '山西',
#     '河北',
#     '安徽',
#     '河南',
#     '山东',
#     '西藏']
# data = [(i, random.randint(50, 150)) for i in province]

# geo = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("", data)
# )
# geo.render_notebook()


#MAP-地图
# province = [
#     '广东',
#     '湖北',
#     '湖南',
#     '四川',
#     '重庆',
#     '黑龙江',
#     '浙江',
#     '山西',
#     '河北',
#     '安徽',
#     '河南',
#     '山东',
#     '西藏']
# data = [(i, random.randint(50, 150)) for i in province]

# map_ = (
#     Map()
#     .add("", data, 'china')
# )
# map_.render_notebook()


#饼图
# cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
# data = [123, 153, 89, 107, 98, 23]

# pie = (Pie()
#        .add('', [list(z) for z in zip(cate, data)])
#        )

# pie.render_notebook()


#词云图

words = [
    ("hey", 230),
    ("jude", 124),
    ("dont", 436),
    ("make", 255),
    ("it", 247),
    ("bad", 244),
    ("Take", 138),
    ("a sad song", 184),
    ("and", 12),
    ("make", 165),
    ("it", 247),
    ("better", 182),
    ("remember", 255),
    ("to", 150),
    ("let", 162),
    ("her", 266),
    ("into", 60),
    ("your", 82),
    ("heart", 173),
    ("then", 365),
    ("you", 360),
    ("can", 282),
    ("start", 273),
    ("make", 265),
]


wc = (
    WordCloud()
    .add("", words)
)

wc.render_notebook()


#表格
from pyecharts.components import Table


table = Table()

headers = ["City name", "Area", "Population", "Annual Rainfall"]
rows = [
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Adelaide", 1295, 1158259, 600.5],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
]
table.add(headers, rows)

table.render_notebook()


