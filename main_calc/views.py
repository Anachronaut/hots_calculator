from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.core import serializers
from .models import Hero
from .forms import AllySelectForm, OpponentSelectForm, AllyBanForm, OpponentBanForm
import json
from hots_calculator import settings


#TODO: Implement sessions, cookies to stop using one set of global dicts for every user
removed_form_key = {}
removed_hero_key = {}

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

def hero_update(request):
    print('REQUEST:',request)
    hero_id = request.GET.get('hero', None)
    form_id = request.GET.get('formid', None)
    print(Hero.objects.all())
    selected = False
    if hero_id != '':
        hero = Hero.objects.filter(id=hero_id).values()
        print('HERO:',hero)
        hero_img = hero[0]['image']
        hero_name = hero[0]['name']
        hero_winr = hero[0]['win_rate']
        hero_wins = hero[0]['win_total']
        hero_loss = hero[0]['loss_total']
        hero_gplay = hero[0]['games_played']

        ally_1 = Hero.objects.filter(name=hero[0]['ally_1']).values()
        ally_img1 = ally_1[0]['image']
        ally_name1 = ally_1[0]['name']
        ally_win1 = hero[0]['ally_1_win']
        ally_2 = Hero.objects.filter(name=hero[0]['ally_2']).values()
        ally_img2 = ally_2[0]['image']
        ally_name2 = ally_2[0]['name']
        ally_win2 = hero[0]['ally_2_win']
        ally_3 = Hero.objects.filter(name=hero[0]['ally_3']).values()
        ally_img3 = ally_3[0]['image']
        ally_name3 = ally_3[0]['name']
        ally_win3 = hero[0]['ally_3_win']
        ally_4 = Hero.objects.filter(name=hero[0]['ally_4']).values()
        ally_img4 = ally_4[0]['image']
        ally_name4 = ally_4[0]['name']
        ally_win4 = hero[0]['ally_4_win']
        ally_5 = Hero.objects.filter(name=hero[0]['ally_5']).values()
        ally_img5 = ally_5[0]['image']
        ally_name5 = ally_5[0]['name']
        ally_win5 = hero[0]['ally_5_win']

        enemy_1 = Hero.objects.filter(name=hero[0]['enemy_1']).values()
        enemy_img1 = enemy_1[0]['image']
        enemy_name1 = enemy_1[0]['name']
        enemy_win1 = hero[0]['enemy_1_win']
        enemy_2 = Hero.objects.filter(name=hero[0]['enemy_2']).values()
        enemy_img2 = enemy_2[0]['image']
        enemy_name2 = enemy_2[0]['name']
        enemy_win2 = hero[0]['enemy_2_win']
        enemy_3 = Hero.objects.filter(name=hero[0]['enemy_3']).values()
        enemy_img3 = enemy_3[0]['image']
        enemy_name3 = enemy_3[0]['name']
        enemy_win3 = hero[0]['enemy_3_win']
        enemy_4 = Hero.objects.filter(name=hero[0]['enemy_4']).values()
        enemy_img4 = enemy_4[0]['image']
        enemy_name4 = enemy_4[0]['name']
        enemy_win4 = hero[0]['enemy_4_win']
        enemy_5 = Hero.objects.filter(name=hero[0]['enemy_5']).values()
        enemy_img5 = enemy_5[0]['image']
        enemy_name5 = enemy_5[0]['name']
        enemy_win5 = hero[0]['enemy_5_win']

    if form_id in removed_form_key:
        form_hero = removed_form_key[form_id]
        if form_hero in removed_hero_key and form_id in removed_form_key:
            del removed_hero_key[form_hero]
    if hero_id in removed_hero_key and form_id not in removed_form_key:
        selected = True
    elif hero_id in removed_hero_key and form_id in removed_form_key:
        if form_hero in removed_hero_key:
            del removed_hero_key[form_hero]
        if hero_id in removed_form_key.values():
            selected = True
        else:
            removed_form_key[form_id] = hero_id
        if form_hero in removed_hero_key:
            del removed_hero_key[form_hero]
        del removed_form_key[form_id]
    
    elif hero_id == '':
        hero_name = ''
        hero_winr = ''
        hero_wins = ''
        hero_loss = ''
        hero_gplay = ''
        hero_img = "hero_images/unk.png"
        ally_img1 = "hero_images/unk.png"
        ally_name1 = ''
        ally_win1 = ''
        ally_img2 = "hero_images/unk.png"
        ally_name2 = ''
        ally_win2 = ''
        ally_img3 = "hero_images/unk.png"
        ally_name3 = ''
        ally_win3 = ''
        ally_img4 = "hero_images/unk.png"
        ally_name4 = ''
        ally_win4 = ''
        ally_img5 = "hero_images/unk.png"
        ally_name5 = ''
        ally_win5 = ''
        enemy_img1 = "hero_images/unk.png"
        enemy_name1 = ''
        enemy_win1 = ''
        enemy_img2 = "hero_images/unk.png"
        enemy_name2 = ''
        enemy_win2 = ''
        enemy_img3 = "hero_images/unk.png"
        enemy_name3 = ''
        enemy_win3 = ''
        enemy_img4 = "hero_images/unk.png"
        enemy_name4 = ''
        enemy_win4 = ''
        enemy_img5 = "hero_images/unk.png"
        enemy_name5 = ''
        enemy_win5 = ''

        form_hero = removed_form_key[form_id]
        del removed_hero_key[form_hero]
        del removed_form_key[form_id]

    else:
        removed_form_key[form_id] = hero_id
        removed_hero_key[hero_id] = form_id
    
    data = {
        'is_chosen': selected,
        'hero_id': hero_id,
        'hero_img': hero_img,
        'hero_name': hero_name,
        'hero_winr': hero_winr,
        'hero_wins': hero_wins,
        'hero_loss': hero_loss,
        'hero_gplay': hero_gplay,
        'ally_img1': ally_img1,
        'ally_name1': ally_name1,
        'ally_win1': ally_win1,
        'ally_img2': ally_img2,
        'ally_name2': ally_name2,
        'ally_win2': ally_win2,
        'ally_img3': ally_img3,
        'ally_name3': ally_name3,
        'ally_win3': ally_win3,
        'ally_img4': ally_img4,
        'ally_name4': ally_name4,
        'ally_win4': ally_win4,
        'ally_img5': ally_img5,
        'ally_name5': ally_name5,
        'ally_win5': ally_win5,
        'enemy_img1': enemy_img1,
        'enemy_name1': enemy_name1,
        'enemy_win1': enemy_win1,
        'enemy_img2': enemy_img2,
        'enemy_name2': enemy_name2,
        'enemy_win2': enemy_win2,
        'enemy_img3': enemy_img3,
        'enemy_name3': enemy_name3,
        'enemy_win3': enemy_win3,
        'enemy_img4': enemy_img4,
        'enemy_name4': enemy_name4,
        'enemy_win4': enemy_win4,
        'enemy_img5': enemy_img5,
        'enemy_name5': enemy_name5,
        'enemy_win5': enemy_win5
    }
    return JsonResponse(data)

def reset(request):
    if (request.GET.get('reset-button')):
        removed_form_key.clear()
        removed_hero_key.clear()
    return redirect('homepage')