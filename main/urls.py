from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('about/<str:myname>', views.about),
]

