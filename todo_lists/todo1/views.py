from django.shortcuts import render,redirect
from .models import Details
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['desc']
        date=request.POST['date']
        Details.objects.create(taskname=name,desc=description,date=date)
        return redirect('home')
    data=Details.objects.all()
    context={'title':'Home page',
        'data':data}
    return render(request,'home.html',context)

def update(request,id):
    try:
        if request.method=='POST':
            data=Details.objects.get(id=id)
            data.taskname=request.POST['name']
            data.desc=request.POST['desc']
            data.date=request.POST['date']
            data.save()
            return redirect('home')
    except:
        return  HttpResponse("Data Not Found")
    context={'title':'Update page'}
    return render(request,'update.html',context)
    
def delete(request,id):
    try:
        request.method=='POST'
        data=Details.objects.get(id=id)
        data.delete()
        return redirect('home')
    except:
        return  HttpResponse("Data Not Found")