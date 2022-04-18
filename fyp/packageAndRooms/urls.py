from django.urls import path
from packageAndRooms import views
from .views import Signup, Login, logout


app_name = 'Package_And_Rooms'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about,name='about'),
    path('offers/', views.offers, name= 'offers'),
    path('contact/', views.contact,name='contact'),
    path('single_listing/', views.single_listing, name='single_li'),
    path('signup', Signup.as_view() , name='signup'),
    path('login', Login.as_view() , name='login'),
     path('logout', logout , name='logout')

    
]
