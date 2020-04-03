import pandas as pd
import numpy as np
data1=pd.read_csv('E://project/yuebao/202003/7soc指标.csv')
data2=pd.read_csv('E://project/yuebao/202003/dm.csv')
data3=pd.read_csv('E://project/yuebao/202003/v.csv')
data4=pd.read_csv('E://project/yuebao/202003/90-40.csv')
# 用户充电初始SOC分布1
result1=pd.DataFrame()
percent=[]
temp=data1['startsoc']
label1=['0-9','10-19’','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-100','合计']
sy= np.zeros(11)
for i in temp:
    if i>=0 and i <10:sy[0]+=1
    elif i>=10 and i<20:sy[1]+=1
    elif i>=20 and i<30:sy[2]+=1
    elif i>=30 and i<40:sy[3]+=1
    elif i>=40 and i<50:sy[4]+=1
    elif i>=50 and i<60:sy[5]+=1
    elif i>=60 and i<70:sy[6]+=1
    elif i>=70 and i<80:sy[7]+=1
    elif i >= 80 and i < 90:sy[8] += 1
    elif i >= 90 and i <=100:sy[9] += 1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result1.insert(loc=0,column='行标签1',value=label1)
result1.insert(loc=1,column='频次1',value=sy)
result1.insert(loc=2,column='占比1',value=percent)
# E-HS3用户充电结束SOC分布2
result2=pd.DataFrame()
percent=[]
temp=data1['edsoc']
label2=['0-9','10-19’','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-100','合计']
sy= np.zeros(11)
for i in temp:
    if i>=0 and i <10:sy[0]+=1
    elif i>=10 and i<20:sy[1]+=1
    elif i>=20 and i<30:sy[2]+=1
    elif i>=30 and i<40:sy[3]+=1
    elif i>=40 and i<50:sy[4]+=1
    elif i>=50 and i<60:sy[5]+=1
    elif i>=60 and i<70:sy[6]+=1
    elif i>=70 and i<80:sy[7]+=1
    elif i >= 80 and i < 90:sy[8] += 1
    elif i >= 90 and i <=100:sy[9] += 1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result2.insert(loc=0,column='行标签2',value=label2)
result2.insert(loc=1,column='频次2',value=sy)
result2.insert(loc=2,column='占比2',value=percent)
# 充电时车辆可行驶里程3
result3=pd.DataFrame()
percent=[]
temp=data1['start_sy']
label2=['0-49','50-99','100-149','150-199','200-249','250-299','300-349','350-400','合计']
sy= np.zeros(9)
for i in temp:
    if i>=0 and i <50:sy[0]+=1
    elif i>=50 and i<100:sy[1]+=1
    elif i>=100 and i<150:sy[2]+=1
    elif i>=150 and i<200:sy[3]+=1
    elif i>=200 and i<250:sy[4]+=1
    elif i>=250 and i<300:sy[5]+=1
    elif i>=300 and i<350:sy[6]+=1
    elif i>=350 and i<400:sy[7]+=1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result3.insert(loc=0,column='行标签3',value=label2)
result3.insert(loc=1,column='频次3',value=sy)
result3.insert(loc=2,column='占比3',value=percent)
# 用户充电初始时刻4
result4=pd.DataFrame()
percent=[]
temp=data1['hour']
label4=['0','1','2','3','4','5','6','7','8','9','10','11','12','13',
        '14','15','16','17','18','19','20','21','22','23','合计']
sy= np.zeros(25)
for i in temp:
    if i ==0:sy[0]+=1
    elif i==1:sy[1]+=1
    elif i==2:sy[2]+=1
    elif i==3:sy[3]+=1
    elif i==4:sy[4]+=1
    elif i==5:sy[5]+=1
    elif i==6:sy[6]+=1
    elif i==7:sy[7]+=1
    elif i==8:sy[8]+=1
    elif i==9:sy[9]+=1
    elif i==10:sy[10]+=1
    elif i==11:sy[11]+=1
    elif i==12:sy[12]+=1
    elif i==13:sy[13]+=1
    elif i==14:sy[14]+=1
    elif i==15:sy[15]+=1
    elif i==16:sy[16]+=1
    elif i==17:sy[17]+=1
    elif i==18:sy[18]+=1
    elif i==19:sy[19]+=1
    elif i==20:sy[20]+=1
    elif i==21:sy[21]+=1
    elif i==22:sy[22]+=1
    elif i==23:sy[23]+=1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result4.insert(loc=0,column='行标签4',value=label4)
result4.insert(loc=1,column='频次4',value=sy)
result4.insert(loc=2,column='占比4',value=percent)
# 用户充电时长分布5
result5=pd.DataFrame()
percent=[]
temp=data1['dt']
label5=['0-15','15-30','30-45','45-60','60-75','75-90','90-105','105-120',
        '120-135','135-150','150-165','165-180','>180','合计']
sy= np.zeros(14)
for i in temp:
    if i>=0 and i <15:sy[0]+=1
    elif i>=15 and i<30:sy[1]+=1
    elif i>=30 and i<45:sy[2]+=1
    elif i>=45 and i<60:sy[3]+=1
    elif i>=60 and i<75:sy[4]+=1
    elif i>=75 and i<90:sy[5]+=1
    elif i>=90 and i<105:sy[6]+=1
    elif i>=105 and i<120:sy[7]+=1
    elif i>=120 and i<135:sy[8]+=1
    elif i>=135 and i<150:sy[9]+=1
    elif i>=150 and i<165:sy[10]+=1
    elif i>=165 and i<=180:sy[11]+=1
    elif i>180 :sy[12]+=1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result5.insert(loc=0,column='行标签5',value=label5)
result5.insert(loc=1,column='频次5',value=sy)
result5.insert(loc=2,column='占比5',value=percent)
# 用户充电模式分布6
result6=pd.DataFrame()
percent=[]
temp=data1['Charge_mod']
label6=['1','3','4','5','7','合计']
sy= np.zeros(6)
for i in temp:
    if i ==1:sy[0]+=1
    elif i==3:sy[1]+=1
    elif i==4:sy[2]+=1
    elif i==5:sy[3]+=1
    elif i==7:sy[4]+=1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result6.insert(loc=0,column='行标签6',value=label6)
result6.insert(loc=1,column='频次6',value=sy)
result6.insert(loc=2,column='占比6',value=percent)
# 用户平均单次行程驾驶里程分布8
result7=pd.DataFrame()
percent=[]
temp=data2['dmil']
label7=['0-10','10-20’','20-30','30-40','40-50','50-60','60-70','70-80','80-90',
        '90-100','100-110','110-120','>120','合计']
sy= np.zeros(14)
for i in temp:
    if i>=2 and i <10:sy[0]+=1
    elif i>=10 and i<20:sy[1]+=1
    elif i>=20 and i<30:sy[2]+=1
    elif i>=30 and i<40:sy[3]+=1
    elif i>=40 and i<50:sy[4]+=1
    elif i>=50 and i<60:sy[5]+=1
    elif i>=60 and i<70:sy[6]+=1
    elif i>=70 and i<80:sy[7]+=1
    elif i >= 80 and i < 90:sy[8] += 1
    elif i >= 90 and i <100:sy[9] += 1
    elif i >= 100 and i <110:sy[10] += 1
    elif i >= 110 and i <=120:sy[11] += 1
    elif i>120 and i<400:sy[12]+=1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result7.insert(loc=0,column='行标签7',value=label7)
result7.insert(loc=1,column='频次7',value=sy)
result7.insert(loc=2,column='占比7',value=percent)
# 用户充电间的行驶里程分布7
result8=pd.DataFrame()
percent=[]
temp=data1['gap_mil']
label8=['0-50','50-100','100-150','150-200','200-250','250-300','>300','合计']
sy= np.zeros(8)
for i in temp:
    if i>=0 and i <50:sy[0]+=1
    elif i>=50 and i<100:sy[1]+=1
    elif i>=100 and i<150:sy[2]+=1
    elif i>=150 and i<200:sy[3]+=1
    elif i>=200 and i<250:sy[4]+=1
    elif i>=250 and i<=300:sy[5]+=1
    elif i>300 :sy[6]+=1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result8.insert(loc=0,column='行标签8',value=label8)
result8.insert(loc=1,column='频次8',value=sy)
result8.insert(loc=2,column='占比8',value=percent)
# 不同车速区间消耗占比9
result9=pd.DataFrame()
percent=[]
label9=['0-10','10-20’','20-30','30-40','40-50','50-60','60-70',
        '70-80','80-90','90-100','100-110','110-120','>120','合计']
sy= np.zeros(14)
for i in range(13):
    temp=data3.loc[data3['flag']==(i+1),'ddd']
    sy[i]=sum(temp)
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result9.insert(loc=0,column='行标签9',value=label9)
result9.insert(loc=1,column='频次9',value=sy)
result9.insert(loc=2,column='占比9',value=percent)
# 90-40实际续航里程分布10
result10=pd.DataFrame()
percent=[]
temp=data4.loc[data4['dsoc']==50,'dmil']
label10=['90-100','100-110','110-120','120-130','130-140',
         '140-150’','150-160','160-170','170-180','180-190','合计']
sy= np.zeros(11)
for i in temp:
    if i>=90 and i <100:sy[0]+=1
    elif i>=100 and i<110:sy[1]+=1
    elif i>=110 and i<120:sy[2]+=1
    elif i>=120 and i<130:sy[3]+=1
    elif i>=130 and i<140:sy[4]+=1
    elif i>=140 and i<150:sy[5]+=1
    elif i>=150 and i<160:sy[6]+=1
    elif i>=160 and i<170:sy[7]+=1
    elif i >= 170 and i < 180:sy[8] += 1
    elif i >= 180 and i <=190:sy[9] += 1
    else:continue
counts=sum(sy)
for j in sy:
    percent.append(j/counts)
sy[-1]=counts
percent[-1]=1
result10.insert(loc=0,column='行标签10',value=label10)
result10.insert(loc=1,column='频次10',value=sy)
result10.insert(loc=2,column='占比10',value=percent)

result=pd.concat([result1,result2,result3,result4,result5,result6,result7,result8,result9,result10],axis=1)
# print(result8)
result.to_csv('E://project/yuebao/result202003.csv',encoding='utf-8-sig')
print('完成！')