from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insetion is done')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    To=Topic.objects.all()
    d={'TO':To}
    if request.method=='POST':
        tn=request.POST['topic']
        na=request.POST['name']
        ur=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('insetion is done')
    return render(request,'insert_webpage.html',d)



def insert_access(request):
    Wo=Webpage.objects.all()
    d={'Wo':Wo}
    if request.method=='POST':
        na=request.POST['name']
        da=request.POST['date']
        W=Webpage.objects.get_or_create(name=na)[0]
        W.save()
        A=Access.objects.get_or_create(name=W,date=da)[0]
        A.save()
        return HttpResponse('insetion is done')

    return render(request,'insert_access.html',d)


def select_topic(request):
    To=Topic.objects.all()
    d={'To':To}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        w=Webpage.objects.none()
        for i in tn:
            w=w | Webpage.objects.filter(topic_name=i)
        data={'w':w}
        return render(request,'display_webpage.html',data)
    return render(request,'select_topic.html',d)
def checkbox(request):
    To=Topic.objects.all()
    d={'To':To}
    return render(request,'checkbox.html',d)