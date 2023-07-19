from django.shortcuts import render,redirect
from .models import Courses,FormData,FeedbackData
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

@login_required(login_url='login')
def homepage(request):
    return render(request,'home.html')

@login_required(login_url='login')
def contactpage(request):
    all=FormData.objects.all()
    return render(request,'contact.html',{'abcd':all})

@login_required(login_url='login')
def feedbackpage(request):
    if request.method=='GET':
        feed=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedback.html',{'abcd':feed})
    else:
        FeedbackData(
        feed=request.POST['feedback'],
        user_name=request.POST['user']
        ).save()
        feeds=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedback.html',{'abcd':feeds})

@login_required(login_url='login')
def gallerypage(request):
    return render(request,'gallery.html')

@login_required(login_url='login')
def servicepage(request):
    all=Courses.objects.all()
    return render(request,'service.html',{'abcd':all})

def loginpage(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        userss=request.POST['username']
        pw=request.POST['password']
        userauth=authenticate(username=userss,password=pw)
        if userauth is not None:
            login(request,userauth)
            return redirect(homepage)
        else:
            return HttpResponse('Invalid Login Details')

def logoutpage(request):
    logout(request)
    return redirect(loginpage)

def registerpage(request):
    if request.method=='GET':
        form=RegistrationForm()
        return render(request,'register.html',{'data':form})
    else:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(loginpage)
        else:
            return HttpResponse('Please Recheck Your Details')
