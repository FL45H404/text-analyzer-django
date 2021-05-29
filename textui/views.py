from django.http import HttpResponse
from django.shortcuts import render,redirect
def index(request):
    data='vipul'
    return render(request,'index.html',{'data':'vipul'})
def about(request):
    return HttpResponse('about')