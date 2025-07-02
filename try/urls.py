from django.urls import path
from .views import *
urlpatterns = [
    # path('',tryss,name="tryss"),
    path('', person_create, name='person_create'),
    # path('success/', success_view, name='success'),
    path('list/', person_list, name='person_list'),
]
