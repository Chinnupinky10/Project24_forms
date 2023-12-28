from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def htmlforms(request):

    if request.method=='POST':
        username=request.POST['un']
        return HttpResponse(username)
    return render(request,'htmlforms.html')



    
def create_school(request):

    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST.get('sl')
        sp=request.POST.get('sp')
    

        SO=School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp)

        SO.save()

        return HttpResponse('School data is inserted')
    
    return render(request,'create_school.html')


