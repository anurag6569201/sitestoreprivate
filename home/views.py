from django.shortcuts import render
from home.models import CrousalHome


def home(request):
    crousal_sites=CrousalHome.objects.all()
    context={
        'crousal_sites':crousal_sites,
    }
    return render(request, 'home/home.html',context)