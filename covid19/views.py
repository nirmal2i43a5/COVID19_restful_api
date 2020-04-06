
import requests
import json

from django.shortcuts import render


# Create your views here.
def covid19(request):
    # url = 'https://brp.com.np/covid/nepal.php'
    url = 'https://brp.com.np/covid/country.php'
    url_nepal = 'https://brp.com.np/covid/nepal.php'
    world_data_url = 'https://brp.com.np/covid/alldata.php'
    
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
    
    r = requests.get(world_data_url).json()
    world_total_datas = {
                   
                    'total_cases':r['total_cases'],
                
                    'total_deaths':r['total_deaths'],
                    'new_deaths':r['new_deaths'],
                    'total_recovered':r['total_recovered'],
                    'new_cases':r['new_cases'],
                   
            }
    
    
  
  
    r = requests.get(url).json()
    length = len(r['countries_stat'])#json data length   
    actual_length = length + 1
    world_datas = [] 
  
    
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
       
        # total_cases = corona_datas['total_cases']
        # world_cases = world_cases + int(total_cases.replace(',',''))#if i want to change large string value i.e--> '236828872' to 236828872
        # total = total + int(total_cases)-->This lines give error 
 
        # print("--------------------------------------------------------")
        # print(total_cases)
        # total = total + int(new_deaths)   
        world_datas.append(corona_datas)
    
    context = {'corona_datas':world_datas,
               'nepal_datas':nepal_datas,
               'world_total_datas':world_total_datas
               
               }
    return render(request,'covid19.html',context)
