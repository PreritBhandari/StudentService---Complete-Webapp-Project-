from django.urls import path
from . import views

urlpatterns = [
    path('', views.informationhome, name='infosec'),
    path('create/', views.CreateInfoSec.as_view(), name='infosec-create'),
    path('list/', views.information, name='infosec-list'),
    path('listuser/', views.ListInfoSec.as_view(), name='infosec-list-user'),

]
