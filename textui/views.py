from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    uppercase=request.POST.get('uppercase','off')
    removepunc=request.POST.get('removepunc','off')
    newlineremover=request.POST.get('newlineremover','off')
    result=''
    print(len(djtext))
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
    if (newlineremover == "on"):
        result = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                result = result + char

        params ={'res':'result','result':result}

    if(removepunc!='on' and uppercase!='on' and newlineremover!='on'):
        return HttpResponse('please select at least one service')
    return render(request,'index.html',params)
    