from django.urls import path
from app2.views import *
app_name='aa'
urlpatterns=[
    path('ram/',ram,name='ram'),
     path('sam/',sam,name='sam'),
]