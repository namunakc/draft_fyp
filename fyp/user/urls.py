from django.urls import path
from .views import logoutFun, home, main, signup_ajax_function, signin_ajax_function

app_name = 'user'
urlpatterns = [
   path('reg/',signup_ajax_function,name='reg'),
   path('login/',signin_ajax_function,name='login'),
   path('',main,name='main'),
   path('home/',home,name='home'),
   path('logout/',logoutFun,name='logout')

]