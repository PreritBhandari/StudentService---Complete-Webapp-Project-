from django.urls import path
from .views import PostListView, PostCreateView,PostUpdateView, PostDeleteView
from . import views
from .views import FeeListView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('rate/new/', PostCreateView.as_view(), name='post-create'),
    path('rate/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('rate/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('rate/', PostListView.as_view(), name='blog-rate'),
    path('account/list', FeeListView.as_view(), name='account-list'),
]
