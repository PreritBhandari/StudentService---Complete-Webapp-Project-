from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, AddFeeCreateView, AddFeeListView
from . import views
from .views import FullfeeCreateView, FullfeeUpdateView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('rate/new/', PostCreateView.as_view(), name='post-create'),
    path('rate/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('rate/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('rate/', PostListView.as_view(), name='blog-rate'),
    path('account/list', AddFeeListView.as_view(), name='account-list'),
    path('account/add-fee/add/', FullfeeCreateView.as_view(), name='add-fee'),
    path('account/add-fee/add/<int:pk>/update', FullfeeUpdateView.as_view(), name='full-fee-update'),
    path('account/AddFee/', AddFeeCreateView.as_view(), name='AddFee')
]
