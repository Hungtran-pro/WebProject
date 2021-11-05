from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	path('<str:room_name>/', views.Room.as_view(), name='room'),
	path('<str:username>/profile', views.Profile.as_view(), name='username'),
	# path('<str:username>/', views.Room.as_view(), name='username'),
	# url(r'^(?P<user_id>\d+)/profile/', views.Profile.as_view(), name='username'),
	# # url(r'^<str:username>/profile/', views.Receiver_Profile.as_view(), name='receiver'),
	path('<str:username>/receiverprofile', views.Receiver_Profile.as_view(), name='receiver'),
	url(r'^(?P<user_id>\d+)/profile/edit$', views.EditProfile, name='editprofile'),
	# url(r'^profile/(?P<username>\w+)/$', views.Profile.as_view(), name='user_profile'),
	path('api/messages/<str:room_name>/', views.MessagesAPIView.as_view(), name="messages"),
]