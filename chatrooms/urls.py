from django.urls import path
from . import views,user_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	path('<str:room_name>/', views.Room.as_view(), name='room'),
	url(r"^register$",user_views.Register_User,name= 'register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('api/messages/<str:room_name>/', views.MessagesAPIView.as_view(), name="messages"),
]