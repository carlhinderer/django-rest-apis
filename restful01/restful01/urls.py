from django.conf.urls import url, include 

urlpatterns = [
    url(r'^', include('toys.urls')),
    url(r'^', include('drones.urls')),
]