from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json, requests


def index(request):
    return render(request, 'index.html')

def current_weather(request):
    
    if request.method == "POST":
        city_name = request.POST.get('city').capitalize()
        print("_"*50)
        print(city_name)
        print("_"*50)
    
        api_key = "832057fb0459061fc996a5a8" #Enter your Api Key
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

        temp = requests.get(complete_url) 
   
       
        x = temp.json() 
        print(x)

        if x["cod"] != "404": 

            y = x["main"] 
            current_temperature = y["temp"] 
            cel = current_temperature - 273
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"] 
            z = x["weather"] 
            lat = x["coord"]["lat"]
            lot = x["coord"]["lon"]
            weather_description = z[0]["description"] 
            weather_description = weather_description.capitalize()

            res = { 
                "result":True,
                "city" : city_name,
                "latitude": lat,
                "longitude" : lot,
                "current_temperature": current_temperature,
                "current_pressure": current_pressure,
                "current_humidiy" : current_humidiy,
                "weather_description" : weather_description,
                "cel": cel,

            
            }
            print(res)
            return render(request,'current_weather.html', context=res)
            
  
    # print following values 
    # print(" Temperature (in kelvin unit) = " +
    #                 str(current_temperature) + 
    #       "\n atmospheric pressure (in hPa unit) = " +
    #                 str(current_pressure) +
    #       "\n humidity (in percentage) = " +
    #                 str(current_humidiy) +
    #       "\n description = " +
    #                 str(weather_description)) 
  
        else:
            res = {
                "result":   False,
                "message" : "City not found...  Try Again",
            }
            print("_"*50)
            print("in else block")
            return render(request,'current_weather.html', context= res)

