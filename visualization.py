# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator , FormatStrFormatter #新增函数
import matplotlib as mpl 
import csv
import jieba
import numpy
from urllib.parse import quote,unquote
from wordcloud import WordCloud,STOPWORDS
from scipy.misc import imread
import pygal
'''
#得分与排名的情况
rank = list()
score = list()
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    rank_str = [row['rank'] for row in reader ]
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    score_str = [row['score'] for row in reader ]
for x in rank_str:
    rank.append(int(x))
for y in score_str:
    score.append(float(y))

plt.gca().invert_yaxis()   #反转y轴
plt.style.use('ggplot')
plt.scatter(score,rank)
plt.xlabel('score')
plt.ylabel('rank')
plt.title('得分和排名')
plt.show()

#得分与电影年份的关系
year = list()
score = list()
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    year_str = [row['year'] for row in reader ]
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    score_str = [row['score'] for row in reader ]
for x in year_str:
    year.append(str(x))
for y in score_str:
    score.append(float(y))

plt.style.use('ggplot')
plt.scatter(year,score)
plt.xlabel('year')
plt.ylabel('score')
plt.title('得分和年份')
plt.show()

#得分与国家的关系
country = list()
score = list()
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    country_str = [row['country'] for row in reader ]
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    score_str = [row['score'] for row in reader ]
for x in country_str:
    country.append(str(x))
for y in score_str:
    score.append(float(y))

plt.style.use('ggplot')
plt.scatter(country,score)
plt.xlabel('country')
plt.ylabel('score')
plt.title('得分和国家')
plt.show()

#电影类别与国家的关系
country = list()
types = list()
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    country_str = [row['country'] for row in reader ]
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    types_str = [row['types'] for row in reader ]
for x in country_str:
    country.append(str(x))
for y in types_str:
    types.append(str(y))

plt.style.use('ggplot')
plt.scatter(country,types)
plt.xlabel('country')
plt.ylabel('types')
plt.title('类别和国家')
plt.show()

#电影国家排名情况
country = list()
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    country_str =' '.join([row['country'] for row in reader ])
    country_list = country_str.split(' ')
#统计
country_set = set(country_list)   #放入set中去除重复数据，得到所有出现的国家
for item in country_set:
    country.append(country_list.count(item))#计数
country_set = list(country_set)

#排序和画图
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 200 #分辨率
plt.xlabel('country')
plt.ylabel('count')
plt.title('国家分析')
plt.tick_params(labelsize=7)   #字体设置

mydict = dict(zip(country,country_set))
mydict_sort = sorted(mydict.items(), key=lambda e:e[0], reverse=True)
mydict_sort = dict(mydict_sort)
plt.bar(list(mydict_sort.values()), list(mydict_sort.keys()),color='lightblue')
plt.show()
'''
#电影类型排名情况
''' 当我们使用matplotlib.plt画图时，如果要输入中文标识，使得在输出图像中显示中文，需要下载需要的字体到代码文件夹下
具体步骤包括：
1.下载一个你需要的字体，例如“微软雅黑”，格式为ttf，将ttf文件放在代码文件夹下
2.修改代码
mpl.rcParams['font.size'] = 15 // 设置字体大小
custom_font = mpl.font_manager.FontProperties(fname='微软雅黑.ttf') // 导入字体文件

plt.figure()
plt.bar([1,2,3,4,5,6,7,8,9,10],[5,6,1,2,7,9,3,8,4,10],alpha = 0.5) 
plt.xlabel(u'样本类别',fontproperties=custom_font) // 在中文字前加英文字母u，并且设置字体
plt.ylabel(u'各类样本数量',fontproperties=custom_font) // 在中文字前加英文字母u，并且设置字体
plt.show()
'''
types = list()
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    types_str =' '.join([row['types'] for row in reader ])
    types_list = types_str.split(' ')
#统计
types_set = set(types_list)   #放入set中去除重复数据，得到所有出现的类型
print (types_set)
for item in types_set:
    types.append(types_list.count(item))#计数
types_set = list(types_set)
types_set.remove('types')
#排序和画图
custom_font = mpl.font_manager.FontProperties(fname='msyh.ttf') #导入字体文件
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 200 #分辨率
plt.xlabel(u'types',fontproperties=custom_font)
plt.ylabel(u'count',fontproperties=custom_font)
plt.title(u'电影类型分析',fontproperties=custom_font)
plt.tick_params(labelsize=7)   #字体设置

mydict = dict(zip(types,types_set))
mydict_sort = sorted(mydict.items(), key=lambda e:e[0], reverse=True)
mydict_sort = dict(mydict_sort)
plt.bar(list(mydict_sort.values()), list(mydict_sort.keys()),color='blue')
plt.show()


'''
#歌曲quote词云图
text = " " 
with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    quote_str =" ".join([row['quote'] for row in reader ])
text = " ".join(jieba.lcut(str(quote_str)))
cat = imread("cat.jpg")
stopwords = set(STOPWORDS)
stopwords.add("Pinocchio")
w = WordCloud(font_path='C:\Windows\Fonts\simkai.ttf', background_color="white",width=1000, height=860,max_font_size=80,min_font_size=8,max_words=88,stopwords=stopwords,mask = cat)
w.generate(text)
w.to_file('quote.jpg')
'''
'''
#设置绘图窗口的尺寸
#plt.figure(dpi=1920*1080,figsize=(10,6))

#绘制直方图，对结果进行可视化（另一种绘制直方图的方式）

hist = pygal.Bar()
hist = "An Analysis of the Proportion of Film Types."
hist.x_labels = country_set
hist.x_title = 'country'
hist.y_title = 'Proportion'
#hist.add('美国',数量)
'''