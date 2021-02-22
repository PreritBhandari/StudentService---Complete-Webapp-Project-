from django.urls import path
from . import views

urlpatterns = [
    path('', views.information, name='infosec'),
    path('create/', views.CreateInfoSec.as_view(), name='infosec-create'),

]
