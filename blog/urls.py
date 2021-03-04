from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, AddFeeCreateView, AddFeeListView, \
    AddFeeUpdateView, ViewFeeTrans
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('blog/', PostListView.as_view(), name='blog-post'),
    path('account/list', AddFeeListView.as_view(), name='account-list'),

    path('account/AddFee/', AddFeeCreateView.as_view(), name='AddFee'),
    path('account/list/<int:pk>/update/', AddFeeUpdateView.as_view(), name='fee-update'),

    # for users view transactions
    path('account/list/trans', ViewFeeTrans.as_view(), name='fee-trans')

]
