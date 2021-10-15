from django.contrib.auth import authenticate,login
from django.shortcuts import redirect,render,HttpResponseRedirect
from .forms import Register, Login
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
def Login_User(request):
    form = Login
    message=''
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
        if user:
            login(request,user)
            if request.GET.get('next') :
                return HttpResponseRedirect(request.GET.get('next'))
            return redirect('index')
        else:
            message="Your Username or Password is wrong!!"
    return render(
        request=request,
        template_name='user/login.html',
        context={
            'form'   : form,
            'message': message

        }
    )
           