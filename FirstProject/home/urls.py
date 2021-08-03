from django.contrib import admin
from django.urls import path, include
from home import views
# me123456

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
]
