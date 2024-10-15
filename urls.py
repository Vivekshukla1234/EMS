from django.urls import path
from .views import *

urlpatterns = [
    path('home/',view_home),
    path('show/',view_show),
    path('dtl/',view_dtl)
]

