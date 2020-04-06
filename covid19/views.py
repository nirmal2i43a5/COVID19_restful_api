
import requests
import json

from django.shortcuts import render


# Create your views here.
def covid19(request):
    # url = 'https://brp.com.np/covid/nepal.php'
    url = 'https://brp.com.np/covid/country.php'
    url_nepal = 'https://brp.com.np/covid/nepal.php'
    
    r = requests.get(url_nepal).json()
    
    nepal_datas = {
                    'country_name':r['latest_stat_by_country'][0]['country_name'],
                    'total_cases':r['latest_stat_by_country'][0]['total_cases'],
                    'active_cases':r['latest_stat_by_country'][0]['active_cases'],
                    'total_deaths':r['latest_stat_by_country'][0]['total_deaths'],
                    'new_deaths':r['latest_stat_by_country'][0]['new_deaths'],
                    'total_recovered':r['latest_stat_by_country'][0]['total_recovered'],
                    'new_cases':r['latest_stat_by_country'][0]['new_cases'],
                    'serious_critical':r['latest_stat_by_country'][0]['serious_critical']
            }
  
    # print(len(r['countries_stat']))#find length of json
    
    # country_dict = json.loads(r)
    # print(country_dict)
    # print(len(country_dict))
    # # print(len(r))
    r = requests.get(url).json()
    length = len(r['countries_stat'])#json data length   
    actual_length = length + 1
    world_datas = [] 
    world_cases = 0
    world_deaths = 0
    world_recovered = 0
    
    for i in range(0,2):
    
        r = requests.get(url).json()
    
        corona_datas = {
                    'country_name':r['countries_stat'][i]['country_name'],
                    'total_cases':r['countries_stat'][i]['cases'],
                    'active_cases':r['countries_stat'][i]['active_cases'],
                    'total_deaths':r['countries_stat'][i]['deaths'],
                    'new_deaths':r['countries_stat'][i]['new_deaths'],
                    'total_recovered':r['countries_stat'][i]['total_recovered'],
                    'new_cases':r['countries_stat'][i]['new_cases'],
                    'serious_critical':r['countries_stat'][i]['serious_critical']
            }
       
        total_cases = corona_datas['total_cases']
        world_cases = world_cases + int(total_cases.replace(',',''))#if i want to change large string value i.e--> '236828872' to 236828872
        # total = total + int(total_cases)-->This lines give error 
        total_deaths = corona_datas['total_deaths']
        
        world_deaths = world_deaths + int(total_deaths.replace(',',''))
        
        total_recovered = corona_datas['total_recovered']
        world_recovered = world_recovered + int(total_recovered.replace(',',''))
       
        # print("--------------------------------------------------------")
        # print(total_cases)
        # total = total + int(new_deaths)   
        world_datas.append(corona_datas)
    
    context = {'corona_datas':world_datas,
               'total_deaths':world_deaths,
               'total_cases':world_cases,
               'total_recovered':world_recovered,
               'nepal_datas':nepal_datas
               }
    return render(request,'covid19.html',context)
