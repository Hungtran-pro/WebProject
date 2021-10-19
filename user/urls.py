from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.forms import AuthenticationForm
urlpatterns=[
    path('login/',LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]