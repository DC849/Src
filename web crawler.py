from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import csv

rank = 1
def write_one_page(soup):
    global rank
    
    for k in soup.find('div',class_='article').find_all('div',class_='info'):
        name = k.find('div',class_='hd').find_all('span')#电影名字
        score = k.find('div',class_='star').find_all('span')#分数
        inq = k.find('p',class_='quote').find('span')#一句话简介
        #抓取年份、国家
        actor_infos_html = k.find(class_='bd')
        #strip() 方法用于移除字符串头尾指定的字符（默认为空格）
        actor_infos = actor_infos_html.find('p').get_text().strip().split('\n')
        actor_infos1 = actor_infos[0].split('\xa0\xa0\xa0')
        director = actor_infos1[0][3:]
        role = actor_infos[1]
        year_area = actor_infos[1].lstrip().split('\xa0/\xa0')
        year = year_area[0]
        country = year_area[1]
        types = year_area[2]

        print(rank,name[0].string,score[1].string,inq.string,year,country,types)
        #写csv       
        write_to_file(rank,name[0].string,score[1].string,year,country,types,inq.string)
    rank = rank+1
def write_to_file(rank,name,score,year,country,types,quote):
    out=open('Top_250_movie.csv', 'a',newline='',encoding='utf-8')
    csv_write=csv.writer(out,dialect='excel')
    csv_write.writerow([str(rank),str(name),str(score),str(year),str(country),str(types),str(quote)])
    
    '''
    with open('Top_250_movie.csv', 'a',encoding='utf-8') as f:
        #csv.write=csv.writer(f,dialext='excel')
        f.writerow(str(rank)+';'+str(name)+';'+str(score)+';'+str(year)+';'+str(country)+';'+str(types)+';'+str(quote)+'\n')
        f.close()
    '''
if __name__ == '__main__':
    with open('Top_250_movie.csv', 'a',newline='',encoding='utf-8') as fp:
            f=csv.writer(fp)
            f.writerow(['rank','name','score','year','country','types','quote'])
    for i in range(20):
        a = i*25
        url = "https://movie.douban.com/top250?start="+str(a)+"&filter="
        f = requests.get(url)               
        soup = BeautifulSoup(f.content, "lxml")
        write_one_page(soup)
