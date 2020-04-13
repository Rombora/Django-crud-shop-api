from django.urls import path, include
from rest_framework import routers

from . import views


###

# from django.conf.urls import url
# from web.views import *
# from .views import my_view

urlpatterns = (
    # path('authe/', my_view, name='authe'),
    # 'web',




    path('product/', views.IndexView.as_view(), name='index'),
    # path('product/list/', views.ProductListView.as_view(), name='product_manager_product_list'),
    path('', views.ProductListView.as_view(), name='product_manager_product_list'), 
    path('product/create/', views.ProductCreateView.as_view(), name='product_manager_product_create'),
    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_manager_product_detail'),
    path('product/update/<slug:slug>/', views.ProductUpdateView.as_view(), name='product_manager_product_update'),
    path('product/delete/<slug:slug>/', views.ProductDeleteView.as_view(), name='product_manager_product_delete'),

    ###################
    path('accounts/signup/', views.SignUpView.as_view(), name='product_manager_signup'),
    path('accounts/login/', views.LoginView.as_view(), name='product_manager_login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='product_manager_logout'),



    # url(r'^login/$', LoginView.as_view(), name='web-login'),
)

urlpatterns += (
    path('category/', views.CategoryListView.as_view(), name='product_manager_category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='product_manager_category_create'),
    path('category/detail/<slug:slug>/', views.CategoryDetailView.as_view(), name='product_manager_category_detail'),
    path('category/update/<slug:slug>/', views.CategoryUpdateView.as_view(), name='product_manager_category_update'),
    path('category/delete/<slug:slug>/', views.CategoryDeleteView.as_view(), name='product_manager_category_delete'),
)

