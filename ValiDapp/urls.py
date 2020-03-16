from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('createvirus', views.create_virus),
    path('allviruses', views.show_all)
]