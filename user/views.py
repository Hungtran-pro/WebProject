from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect,render,HttpResponseRedirect
from django.views.generic.base import TemplateView
from .forms import Register,EditProfile
from .models import MyUser
def Register_User(request):
    form = Register
    message=''
    if request.method == 'POST':
        form =Register(request.POST)
        if form.is_valid():
            form.save_user()
            return redirect('login')
    return render(
        request=request,
        template_name='user/register.html',
        context={
            'form':form,
            'message':message
        }
    )

def edit(request):
    if request.method=='POST':
        user_form=EditProfile(request.POST,instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect("index")
    else:
        user_form=EditProfile(instance=request.user)	
    list_user=MyUser.objects.exclude(id=request.user.id).values('username','first_name','last_name','sex')
    return render(
        request=request,
        template_name='user/edit_profile.html',
        context={
            'user_form':user_form,
            'list_user':list_user
        }
    )