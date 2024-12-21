#Common imports for django
#Allows the creation of paths, the directives for the website. ex. challenges/about-us is the path
from django.urls import path
from . import views #imports the views from hte whole project allowing them to be pulled from their app and used in the project
#Dynamic pathing for the views using If-Else statements.
urlpatterns = [
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge, name = "month-challenge"),
    path("", views.index, name="index") #Allows for dynamic pathing in order to build out the args in views. 
]
