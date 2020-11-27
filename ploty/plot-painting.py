import requests,openpyxl
from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import random
import datetime
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

#
wb1=openpyxl.load_workbook('c:\\Users\\btr\\Desktop\\xmind-technology\\ploty\\2020-9-23-share.xlsx')
sheet=wb1['new title']


x_data = []
y_data = []
indestry='饮料制造'
indestry_list=['水泥制造','白色家电','化学制药','饮料制造']

for i in sheet:
    if i[20].value==indestry:
        x_data.append(i[1].value)
        y_data.append(i[2].value)
wb1.close()


#直方图
bar = (Bar(init_opts=opts.InitOpts(theme='chalk',width='1500px', height='600px'))
       .add_xaxis(x_data)
       .add_yaxis('2020-09-23', y_data)
       .set_global_opts(title_opts=opts.TitleOpts(title=indestry+'_市盈率对比'),
                        yaxis_opts=opts.AxisOpts(name='市盈率', 
                                type_="value",
                                #添加分隔线
                                splitline_opts=opts.SplitLineOpts(is_show=True, 
                                    linestyle_opts=opts.LineStyleOpts(type_='dashed')))
            )           
      )

bar.render_notebook()
