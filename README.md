# controlbymyhobby
This example is used to crawl the weather conditions of the last week at 'http://www.weather.com.cn/textFC/'+province+'.shtml', use the line chart to reflect the temperature change trend, and the horizontal axis displays the weather conditions Sunny, cloudy, light rain, etc.), all data comes from this website to ensure that the data is true and can be displayed in real time,
E.g
http://www.weather.com.cn/textFC/sahnghai.shtml Weather in Shanghai

def weather_info (html): # Crawl weather data
def date_info (html): #Crawl date
def writedata (): #Write to weather.csv
def get_info (province): #Crawl weather conditions in specific provinces
def analysis (province, city_name): # Data cleaning, data analysis
#Data Display
plt.rcParams ['font.sans-serif'] = ['SimHei'] #solve Chinese display problems
plt.rcParams ['axes.unicode_minus'] = False #Solve the problem of negative coordinate display
 






Main function
print ('Please input the location (in Pinyin), city (in Chinese) of the place you want to query in turn: (Enter a value and press Enter)')
province = input ('')
city ​​= input ('')
try:
    analysis (province, city)
except:
    print ('You entered the wrong location')

#Crawling weather data
for city in soup.find_all ('div', class _ = 'conMidtab3'):
      for city_n in city.find_all ('td', {"width": "83", "height": "23"}):
                city_name.append (city_n.find ('a'). string)
      for weather in city.find_all ('td', width = "89"):
                city_day_weather.append (weather.string)
      for weather in city.find_all ('td', width = "162"):
               wind_day_direction.append (weather.find_all ('span') [0] .string)
               wind_day_scale.append (weather.find_all ('span') [1] .string)
      for weather in city.find_all ('td', width = "92"):
                max_day_temperature.append (weather.string)
      for weather in city.find_all ('td', width = "98"):
                city_night_weather.append (weather.string)
      for weather in city.find_all ('td', width = "177"):
                   wind_night_direction.append (weather.find_all ('span') [0] .string)
                wind_night_scale.append (weather.find_all ('span') [1] .string)
      for weather in city.find_all ('td', width = "86"):
                min_night_temperature.append (weather.string)
