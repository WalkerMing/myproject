import asyncio
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Scatter3D

# # 配置 config
config_xAxis3D = "X"
config_yAxis3D = "Y"
config_zAxis3D = "Z"
config_color = "fiber"
config_symbolSize = "vitaminc"

# 构造数据
data=pd.read_csv('E:/project/test/3dplot/data2.csv')
listd=[]
print('数据量：',len(data))
for xyz in range(len(data)):
    temp= data.iloc[xyz,0:3].tolist()
    listd.append(temp)
# print(listd)
print('数据解析完成！')

(
    Scatter3D(
        init_opts=opts.InitOpts(width="1440px", height="720px")
    )  # bg_color="black"
    .add(
        series_name="",
        data=listd,
        xaxis3d_opts=opts.Axis3DOpts(
            name=config_xAxis3D,
            type_="value",
            # textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        yaxis3d_opts=opts.Axis3DOpts(
            name=config_yAxis3D,
            type_="value",
            # textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        zaxis3d_opts=opts.Axis3DOpts(
            name=config_zAxis3D,
            type_="value",
            # textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
    )
    .set_global_opts(
        visualmap_opts=[
            opts.VisualMapOpts(
                type_="color",
                is_calculable=True,
                dimension=1,
                pos_top="10",
                max_=4/2,
                range_color=[
                    "#1710c0",
                    "#0b9df0",
                    "#00fea8",
                    "#00ff0d",
                    "#f5f811",
                    "#f09a09",
                    "#fe0300",
                ],
            ),
            opts.VisualMapOpts(
                type_="size",
                is_calculable=True,
                dimension=2,
                pos_bottom="10",
                max_=4/2,
                range_size=[2, 2],
            ),
        ]
    )
    .render("E://project/test/3dplot/scatter3d.html")
)
print('绘图完成')