from bahuballi2.views import *
from django.urls import path
app_name='nai'
urlpatterns=[
    path('traggic/',traggic,name='traggic'),
]