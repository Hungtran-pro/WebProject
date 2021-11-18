from django import forms
from django.conf.urls import url
from django.contrib.auth import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.forms import fields, widgets
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import Message
from django.urls import reverse
from django.views.generic.edit import UpdateView
class Index(LoginRequiredMixin,TemplateView):
	login_url= reverse_lazy('login')
	template_name = 'chatrooms/index.html'
	
	def get_context_data(self, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['users']=User.objects.exclude(id=self.request.user.id).values('username','first_name','last_name')
		return context

	def get_queryset(self):
		all_users = User.objects.all()
		search = self.request.GET.get('search')
		if search:
			all_users=User.objects.filter(
        	Q(first_name__icontains=search) |
			Q(last_name__icontains=search))
		return all_users

class Room(LoginRequiredMixin,TemplateView):
	template_name = 'chatrooms/room.html'
	
	def dispatch(self, request, *args, **kwargs):
		receiver_username = kwargs['room_name'].replace(
			request.user.username,""
		).replace(
			"-",""	
		)
		kwargs['receiver'] =get_object_or_404(User,username=receiver_username)
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['receiver']= kwargs['receiver']
		return context

class MessagesAPIView(View):

    def get(self, request, room_name):
        users = User.objects.filter(username__in=room_name.split('-'))
        result = Message.objects.filter(
            Q(sender=users[0], receiver=users[1]) | Q(sender=users[1], receiver=users[0])
        ).annotate(
            username=F('sender__username'), message=F('content'),
        ).order_by('timestamp').values('username', 'message', 'timestamp')

        return JsonResponse(list(result), safe=False)

class Profile(LoginRequiredMixin,TemplateView):
	template_name = 'profile/profile.html'
	
	def get_context_data(self, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['users']=User.objects.exclude(id=self.request.user.id).values('username','first_name','last_name')
		return context
			
	def get_queryset(self):
		all_users = User.objects.all()
		search = self.request.GET.get('search')
		if search:
			all_users=User.objects.filter(
        	Q(first_name__icontains=search) |
			Q(last_name__icontains=search))
		return all_users

class Receiver_Profile(LoginRequiredMixin,TemplateView):
	models = Message
	template_name = 'profile/receiver_profile.html'
	context_object_name='receiver_profile'
	def dispatch(self, request, *args, **kwargs):
		receiver_username = kwargs['username']
		kwargs['receiver'] =get_object_or_404(User,username=receiver_username)
		return super().dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['receiver']= kwargs['receiver']
		context['users']=User.objects.exclude(id=self.request.user.id).values('username','first_name','last_name')
		return context











