from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    # other URL patterns for your documents app
]
