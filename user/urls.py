from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.conf.urls import url
from . import views
urlpatterns=[
    path('login/',LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm),name='login'),
    url(r"^register$",views.Register_User,name= 'register'),
    path('logout/',LogoutView.as_view(),name='logout')
]