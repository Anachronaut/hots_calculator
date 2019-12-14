from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.core import serializers
from .models import Hero
from .forms import AllySelectForm, OpponentSelectForm, AllyBanForm, OpponentBanForm
import json
from hots_calculator import settings


removed = []

def homepage(request):
    ally_select_form1 = AllySelectForm(prefix="ally_select_form1")
    ally_select_form2 = AllySelectForm(prefix="ally_select_form2")
    ally_select_form3 = AllySelectForm(prefix="ally_select_form3")
    ally_select_form4 = AllySelectForm(prefix="ally_select_form4")
    ally_select_form5 = AllySelectForm(prefix="ally_select_form5")
    ally_ban_form1 = AllyBanForm(prefix="ally_ban_form1")
    ally_ban_form2 = AllyBanForm(prefix="ally_ban_form2")
    ally_ban_form3 = AllyBanForm(prefix="ally_ban_form3")
    opp_select_form1 = OpponentSelectForm(prefix="opp_select_form1")
    opp_select_form2 = OpponentSelectForm(prefix="opp_select_form2")
    opp_select_form3 = OpponentSelectForm(prefix="opp_select_form3")
    opp_select_form4 = OpponentSelectForm(prefix="opp_select_form4")
    opp_select_form5 = OpponentSelectForm(prefix="opp_select_form5")
    opp_ban_form1 = OpponentBanForm(prefix="opp_ban_form1")
    opp_ban_form2 = OpponentBanForm(prefix="opp_ban_form2")
    opp_ban_form3 = OpponentBanForm(prefix="opp_ban_form3")
    return render(
    request, 
    'home.html', {'ally_select_form1': ally_select_form1, 
    'ally_ban_form1': ally_ban_form1, 'opp_select_form1': opp_select_form1, 
    'opp_ban_form1': opp_ban_form1, 'ally_select_form2': ally_select_form2, 
    'ally_ban_form2': ally_ban_form2, 'opp_select_form2': opp_select_form2, 
    'opp_ban_form2': opp_ban_form2, 'ally_select_form3': ally_select_form3, 
    'ally_ban_form3': ally_ban_form3, 'opp_select_form3': opp_select_form3, 
    'opp_ban_form3': opp_ban_form3, 'ally_select_form4': ally_select_form4, 
    'opp_select_form4': opp_select_form4, 'ally_select_form5': ally_select_form5, 
    'opp_select_form5': opp_select_form5}
    )

def validate_hero(request):
    hero_id = request.GET.get('hero', None)
    if hero_id != '':
        hero = Hero.objects.filter(id=hero_id).values()
        hero_image = hero[0]['image']
        
    selected = False
    if hero_id in removed:
        selected = True
    elif hero_id == '':
        hero_image = "hero_images/unk.png"
    else:
        removed.append(hero_id)
    print(removed)
    data = {
        'is_chosen': selected,
        'hero_id': hero_id,
        'hero_image': hero_image
    }
    return JsonResponse(data)

def reset(request):
    if (request.GET.get('reset-button')):
        del removed[:]
        print(removed)
    else:
        print('!')
    return redirect('homepage')