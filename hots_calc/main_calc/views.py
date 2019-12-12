from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Hero
#from .forms import HeroSelectForm

def homepage(request):
    heroes = Hero.objects.all().order_by('popularity').reverse()
    if request.method == 'GET':
        images = request.GET.getlist('image')
        return render(request, 'home.html', {'heroes': heroes, 'images': images})
    else:
        return render(request, 'home.html', {'heroes': heroes})
    