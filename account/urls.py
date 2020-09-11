from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
    path('logout',views.logout_view, name="logout"),
]