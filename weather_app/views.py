 
import requests
from django.shortcuts import render,get_object_or_404,redirect
from .models import City
from .forms import CityForm
from django.contrib import messages

def weather_api(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=08d0a6c40b18002e648ea80372446d3a'#api url
    #units=imperial means getting fahrenheit as temperature
    #q = {}--->It holds cities
    # city = 'Kathmandu'
   #r is the dictionary as json is in json format
    err_msg = ''#global variable should be used
    message = ''
    message_class = ''
  
   

    if request.method == 'POST':
        form = CityForm(request.POST)
        
        
        if form.is_valid():
            new_city = form.cleaned_data['name']#new city input
            existing_city_count = City.objects.filter(name=new_city).count()
            
                
            if existing_city_count == 0:#it means enter city does not exists already .so i can add that city---
                r = requests.get(url.format(new_city)).json()#for particular city

                if r['cod'] == 200:#if we look at the json data of all the city then cod for all the city is 200---
                                            # if city dont have such code then it cit does not exists in the world
                    form.save()#save to database only if exists
                        
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
            
        else:
            message = 'City added successfully!'
            message_class = 'is-success'
           

    form = CityForm()

    cities = City.objects.all()
    
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()#r is dictionary
    
      
    
    
        city_weather = {
                
                'city' : city.name,
               
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon']
                }
        
        weather_data.append(city_weather)
     
	   
	
  
    context = {'weather_data' : weather_data,'form':form,
               'message':message,
               'messsage_class':message_class}

    # context = {'form' : form}
    
    return render(request,'weather.html',context)



def delete(request,city_name):
    weather_data = get_object_or_404(City,name=city_name)
    
    weather_data.delete()
    messages.error(request,'Successfully deleted ! ',extra_tags="alert")
    
    return redirect('/weather?deleted successfully')

   

        