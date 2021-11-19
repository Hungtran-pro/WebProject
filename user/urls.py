from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
urlpatterns=[
    path('login/',LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm),name='login'),
    url(r"^register$",views.Register_User,name= 'register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    url(r"^change_password$",auth_views.PasswordChangeView.as_view(template_name="user/change_password.html"),name='change_password'),
    url(r"^edit_profile$",views.edit,name='edit_profile')
]