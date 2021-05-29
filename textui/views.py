from django.http import HttpResponse
from django.shortcuts import render,redirect
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.GET.get('text','default')
    uppercase=request.GET.get('uppercase','off')
    removepunc=request.GET.get('removepunc','off')
    result=''
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        result = ""
        for char in djtext:
            if char not in punctuations:
                result = result + char
        params ={'res':'result','result':result}
        djtext = result
    if(uppercase=="on"):
        result=djtext.upper()
        params={'res':'result','result':result}
    if(removepunc!='on' and uppercase!='on'):
        return HttpResponse('please select at least one service')
    return render(request,'index.html',params)
    