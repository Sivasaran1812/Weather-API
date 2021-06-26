from flask import Flask,jsonify
import requests
from bs4 import BeautifulSoup as bs
url="https://www.bbc.com/weather/1264527"

app = Flask(__name__)
@app.route('/getweather/<int:max_speed>')
def getweather(max_speed):
    r=requests.get(url)
    forecast=bs(r.content,"lxml")
    #max_speed = 24 
    #1.Chennai
    wthr_che=forecast.findAll("span",{"class":"wr-wind-speed__value "})
    wthr_che1=forecast.findAll("span",{"class":"wr-value--windspeed wr-value--windspeed--mph"})
    for i in range(2):
        wind_spd_che=wthr_che1[i].text
        wind_spd_che2=list(wind_spd_che.split())
        current_speed_1=int(wind_spd_che2[0])
        if(current_speed_1 <= max_speed):
           result={
               "Current wind speed":current_speed_1,
               "Can drones fly": True
            }
        else:
           result={
             "Current wind speed":current_speed_1,
             "Can drones fly": False
            }      
        return jsonify(result)  
if __name__=="__main__":
    app.run(debug=True)
    