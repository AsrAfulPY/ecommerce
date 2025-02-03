from django.urls import path
from . import views



urlpatterns = [

    path('', views.home, name='home'),                              # 1
    path('about/', views.about, name='about'),                      # _6


    path('login/', views.login_user, name='login'),                      # _7
    path('logout/', views.logout_user, name='logout'),                      # _7

    path('register/', views.register_user, name='register'),                      # _8
    
    path('update_password/', views.update_password, name='update_password'),    # _23

    path('update_user/', views.update_user, name='update_user'),                      # _22

    path('update_info/', views.update_info, name='update_info'),                      # _25



    path('product/<int:pk>', views.product, name='product'),                       #_9

    path('category/<str:foo>/', views.category, name='category'),                       #_10

    path('category_summary/', views.category_summary, name='category_summary'),                       #_20

    path('search/', views.search, name='search'),                      # _26




]
