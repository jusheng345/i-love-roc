from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('up/', include('upload.urls')),
]