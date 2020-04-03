from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
import pandas as pd
import numpy as np
data=pd.read_csv('E://project/yuebao/result202003.csv')
dx1=data.loc[0:9,'行标签1'].tolist()
dy1=data.loc[0:9,'占比1'].tolist()

dx2=data.loc[0:9,'行标签2'].tolist()
dy2=data.loc[0:9,'占比2'].tolist()

dx3=data.loc[0:7,'行标签3'].tolist()
dy3=data.loc[0:7,'占比3'].tolist()

dx4=data.loc[0:23,'行标签4'].tolist()
dy4=data.loc[0:23,'占比4'].tolist()

dx5=data.loc[0:12,'行标签5'].tolist()
dy5=data.loc[0:12,'占比5'].tolist()

tempx6=data.loc[0:4,'行标签6'].tolist()
tempy6=data.loc[0:4,'占比6'].tolist()
dx6=[]
for i in tempx6:
    if i=='1':dx6.append('支流充电')
    elif i=='3':dx6.append('32A交流充电')
    elif i=='4':dx6.append('16A交流充电')
    elif i=='5':dx6.append('10A交流充电')
    elif i=='7':dx6.append('63A交流充电')
    else:continue
dy6=[]
for i in tempy6:
    dy6.append(round(i,4))


dx7=data.loc[0:12,'行标签7'].tolist()
dy7=data.loc[0:12,'占比7'].tolist()

dx8=data.loc[0:6,'行标签8'].tolist()
dy8=data.loc[0:6,'占比8'].tolist()


dx9=data.loc[0:12,'行标签9'].tolist()
dy9=data.loc[0:12,'占比9'].tolist()

dx10=data.loc[0:9,'行标签10'].tolist()
dy10=data.loc[0:9,'占比10'].tolist()
c = (
    Bar()
    .add_xaxis(dx1)
    .add_yaxis('百分比',dy1)

    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户充电初始SOC分布"),
        xaxis_opts=opts.AxisOpts(name='soc区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/1用户充电初始SOC分布.html')
)
c = (
    Bar()
    .add_xaxis(dx2)
    .add_yaxis('百分比',dy2)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="E-HS3用户充电结束SOC分布"),
        xaxis_opts=opts.AxisOpts(name='soc区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/2E-HS3用户充电结束SOC分布.html')
)
c = (
    Bar()
    .add_xaxis(dx3)
    .add_yaxis('百分比',dy3)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="充电时车辆可行驶里程"),
        xaxis_opts=opts.AxisOpts(name='行驶里程区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/3充电时车辆可行驶里程.html')
)
c = (
    Bar()
    .add_xaxis(dx4)
    .add_yaxis('百分比',dy4)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户充电初始时刻分析"),
        xaxis_opts=opts.AxisOpts(name='时刻',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/4用户充电初始时刻分析.html')
)
c = (
    Bar()
    .add_xaxis(dx5)
    .add_yaxis('百分比',dy5)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户充电时长分布"),
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=-30),
            name='时长区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/5用户充电时长分布.html')
)
c = (
    Pie()
    .add("", [list(z) for z in zip(dx6, dy6)], center=["50%", "60%"])
    # .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .set_global_opts(
        legend_opts=opts.LegendOpts(type_="scroll", pos_top='30%',pos_left="10%", orient="vertical"),
        title_opts=opts.TitleOpts(title="用户充电模式分布"),
        xaxis_opts=opts.AxisOpts(name='充电模式',name_location="middle",name_gap=30)
    )
    .render("E://project/yuebao/2003pig/6用户充电模式分布.html")
)
c = (
    Bar()
    .add_xaxis(dx7)
    .add_yaxis('百分比',dy7,)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户平均单次行程驾驶里程分布"),
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=-30),
            name='里程区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/7用户平均单次行程驾驶里程分布.html')
)
c = (
    Bar()
    .add_xaxis(dx8)
    .add_yaxis('百分比',dy8)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户充电间的行驶里程分布"),
        xaxis_opts=opts.AxisOpts(name='里程区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/8用户充电间的行驶里程分布.html')
)

c = (
    Bar()
    .add_xaxis(dx9)
    .add_yaxis('百分比',dy9)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同车速区间耗电占比"),
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=-30),
            name='车速区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/9不同车速区间耗电占比.html')
)
c = (
    Bar()
    .add_xaxis(dx10)
    .add_yaxis('百分比',dy10)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户实际续航里程分布"),
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=-30),
            name='里程区间',name_location="middle",name_gap=30)
    )
    .render('E://project/yuebao/2003pig/10用户实际续航里程分布.html')
)