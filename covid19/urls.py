from django.urls import path
from covid19 import views

app_name = 'covid19_app'

urlpatterns = [
     path('data/',views.covid19,name="covid19")
 ]
 