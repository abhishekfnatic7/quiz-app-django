


from django.urls import path
from . import views
urlpatterns = [
    path('',views.loginPage,name='loginPage'),
    path('logoutpage',views.logoutpage,name='logoutpage'),
    path('home',views.home,name='home'),
    path('addq',views.addq,name='addq'),
    path('register',views.register,name='register'),
   
]
