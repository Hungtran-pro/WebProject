from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	path('<str:room_name>/', views.Room.as_view(), name='room'),
	path('api/messages/<str:room_name>/', views.MessagesAPIView.as_view(), name="messages"),
]