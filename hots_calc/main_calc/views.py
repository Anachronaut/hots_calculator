from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Hero
from .forms import AllySelectForm, OpponentSelectForm, AllyBanForm, OpponentBanForm
import json

'''
def homepage(request):
    heroes = Hero.objects.all().order_by('popularity').reverse()
    if request.method == 'GET':
        images = request.GET.getlist('image')
        return render(request, 'home.html', {'heroes': heroes, 'images': images})
    else:
        return render(request, 'home.html', {'heroes': heroes})
'''

def homepage(request):
    heroes = Hero.objects.all()
    ally_select_form = AllySelectForm()
    ally_ban_form = AllyBanForm()
    opp_select_form = OpponentSelectForm()
    opp_ban_form = OpponentBanForm()
    if request.method == 'POST':
        if ally_select_form.is_valid():
            #hero = get_object_or_404(Hero)
            return redirect('')
        elif ally_ban_form.is_valid():
            return redirect('')
        elif opp_select_form.is_valid():
            return redirect('')
        elif opp_ban_form.is_valid():
            return redirect('')
        else:
            ally_select_form = AllySelectForm()
        ally_select_form = AllySelectForm()
        ally_ban_form = AllyBanForm()
        opp_select_form = OpponentSelectForm()
        opp_ban_form = OpponentBanForm()
    return render(
    request, 
    'home.html', {'ally_select_form': ally_select_form, 
    'ally_ban_form': ally_ban_form, 'opp_select_form': opp_select_form, 
    'opp_ban_form': opp_ban_form, 'heroes': heroes}
    )

def load_select(request):
    initial_data = {

    }

    return JsonResponse(initial_data)



def update_select(request):
    
    if request.method == 'POST':
        request_data = json.loads(request.body)
        update_text = request_data.get('update_text')

        print(request_data,update_text)
        return JsonResponse(update_text)
        
    else:
        return JsonResponse( {"message": "Sorry, the app is not yet finished." } )