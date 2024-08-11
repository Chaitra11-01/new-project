from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginview(request):
    return render(request,'login.html')
def homeview(request):
    return render(request,'home.html')
def aboutview(request):
    return render(request,'about.html')
def contactview(request):
    return render(request,'contact.html')


@login_required(login_url="login page")
def postsview(request):
    return render(request,'posts.html')
