from django.urls import path,include
from Home import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('doctors',views.doctors,name="doctors"),
    path('booking',views.booking,name="booking"),
    path('contacts',views.contacts,name="contacts"),
    path('departments',views.departments,name="departments"),
    
]