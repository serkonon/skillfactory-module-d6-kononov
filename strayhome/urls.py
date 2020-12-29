from django.urls import path
from .views import *

app_name = 'strayhome'
urlpatterns = [
    path('', PetList.as_view(), name='index'),
    path('pet/<int:pk>', PetDetail.as_view(), name='pet_detail'),
    path('donate/', donate, name='donate'),
    path('contact/', contact, name='contact'),
    path('tech_info/', tech_info, name='tech_info'),
]