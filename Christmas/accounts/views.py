from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User,auth


def register(request):

    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']


        # if pass match
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email being used')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)

                    # auth.login(request,user)
                    # messages.success(request,'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request,'You are now registered and can log in...')
                    return redirect('login')

        else:
            messages.error(request,'Password mismatch')
            return redirect('register')
    else:
        print('Error')
        return render(request,'accounts/register.html',{})


def login(request):
    if request.method=='POST':
        return redirect('login')
    else:
        print('Error')
        return render(request,'accounts/login.html',{})


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request,'accounts/dashboard.html',{})