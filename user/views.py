from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect,render,HttpResponseRedirect
from django.views.generic.base import TemplateView
from .forms import Register
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
