from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, AddFeeCreateView, AddFeeListView, \
    AddFeeUpdateView, account, ViewFeeTrans
from . import views
from .views import FullfeeCreateView, FullfeeUpdateView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('blog/', PostListView.as_view(), name='blog-post'),
    path('account/list', AddFeeListView.as_view(), name='account-list'),
    # path('account/', account, name='account'),

    # path('account/add-fee/add/', FullfeeCreateView.as_view(), name='add-fee'),
    # path('account/add-fee/add/<int:pk>/update', FullfeeUpdateView.as_view(), name='full-fee-update'),
    path('account/AddFee/', AddFeeCreateView.as_view(), name='AddFee'),
    path('account/list/<int:pk>/update/', AddFeeUpdateView.as_view(), name='fee-update'),

    # for users view transactions
    path('account/list/trans', ViewFeeTrans.as_view(), name='fee-trans')

]
