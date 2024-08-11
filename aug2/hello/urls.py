from django.urls import path
from hello import views
urlpatterns=[
    path('login',views.loginview,name="loginpage"),
    path('home',views.homeview,name="homepage"),
    path('about',views.aboutview,name="aboutpage"),
    path('contact',views.contactview,name="contactpage"),
    path('posts',views.postsview,name="postspage"),
]