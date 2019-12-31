from urllib import request
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot  as  plt
city_name=[]
city_day_weather=[]
wind_day_direction=[]
wind_day_scale=[]
max_day_temperature=[]
city_night_weather=[]
wind_night_direction=[]
wind_night_scale=[]
min_night_temperature=[]
date=[]
def weather_info(html):      #爬取天气数据
    soup = bs(html, 'html.parser')
    for city in soup.find_all('div',class_='conMidtab3'):
          for city_n in city.find_all('td',{"width":"83","height":"23"}):
                    city_name.append(city_n.find('a').string)
          for weather in city.find_all('td',width="89"):
                    city_day_weather.append(weather.string)
          for weather in city.find_all('td',width="162"):
                    wind_day_direction.append(weather.find_all('span')[0].string)
                    wind_day_scale.append(weather.find_all('span')[1].string)
          for weather in city.find_all('td', width="92"):
                    max_day_temperature.append(weather.string)
          for weather in city.find_all('td', width="98"):
                    city_night_weather.append(weather.string)
          for weather in city.find_all('td', width="177"):
                    wind_night_direction.append(weather.find_all('span')[0].string)
                    wind_night_scale.append(weather.find_all('span')[1].string)
          for weather in city.find_all('td', width="86"):
                    min_night_temperature.append(weather.string)
def date_info(html):#爬取日期
    soup = bs(html, 'html.parser')
    for date_name in soup.find_all('ul', class_="day_tabs"):
        for i in range(7):
            date.append(date_name.find_all('li')[i].string)
def writedata():#写到weather.csv文件中
    dataframe = pd.DataFrame({"city_name": city_name,
                              'city_day_weather': city_day_weather,
                              "wind_day_direction":wind_day_direction,
                            "wind_day_scale":wind_day_scale,
                            "max_day_temperature":max_day_temperature,
                            "city_night_weather":city_night_weather,
                            "wind_night_direction":wind_night_direction,
                            "wind_night_scale":wind_night_scale,
                            "min_night_temperature":min_night_temperature})
    dataframe.to_csv(r"./weather.csv", sep=',')
def get_info(province):#爬取特定省份的天气情况
    url='http://www.weather.com.cn/textFC/'+province+'.shtml'
    info=request.urlopen(url)
    html=info.read().decode('utf-8')
    weather_info(html)
    writedata()
    date_info(html)
def analysis(province,city_name):#数据清洗，数据分析
    get_info(province)
    weather=pd.read_csv(r"./weather.csv")
    city=weather[weather['city_name']==city_name]
    data=pd.concat([city['city_name'],city['max_day_temperature'],city['city_day_weather'],city['min_night_temperature'],city['city_night_weather']],axis=1)
    x_label=['1','2','3','4','5','6','7']
    y=[]
    y1=[]
    if list(data['max_day_temperature'])[0]!='-':
        x=range(len(date))
        for i in range(len(date)):
            a=list(data['max_day_temperature'])[i]
            b=list(data['min_night_temperature'])[i]
            if str(list(data['city_day_weather'])[i])!=str(list(data['city_night_weather'])[i]):
                x_label[i]=date[i]+list(data['city_day_weather'])[i]+'转'+list(data['city_night_weather'])[i]
            else:
                x_label[i]=date[i]+list(data['city_day_weather'])[i]
            y.append(int(a))
            y1.append(int(b))
    else :
        x=range(len(date)-1)
        for i in range(1,len(date),1):
            a=list(data['max_day_temperature'])[i]
            b=list(data['min_night_temperature'])[i]
            if str(list(data['city_day_weather'])[i])!=str(list(data['city_night_weather'])[i]):
                x_label[i-1]=date[i]+list(data['city_day_weather'])[i]+'转'+list(data['city_night_weather'])[i]
            else:
                x_label[i-1]=date[i]+list(data['city_day_weather'])[i]
            y.append(int(a))
            y1.append(int(b))
    #数据显示
    plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False #解决负数坐标显示问题  
    plt.plot(x, y,color='r',marker='^',mec='r',ms=10,mfc='w',label=u'最高温度')
    plt.plot(x, y1,color='b',marker='v',mec='b',ms=10,mfc='w',label=u'最底温度')
    plt.legend() # 让图例生效
    plt.xticks(x, x_label, rotation=45)
    plt.subplots_adjust(bottom=0.25)
    plt.xlabel("天气走势") #X轴标签
    plt.ylabel("摄氏温度") #Y轴标签
    plt.title("温度走势") #标题
    plt.show()
if __name__ == '__main__':
    print('请依次输入要查询地点的所属的省份或者直辖市(用汉语拼音)，城市(用汉字)：(输入一个值后请按回车)')
    province=input('')
    city=input('')
    try:
        analysis(province,city)
    except:
        print('你输入的地点有误')