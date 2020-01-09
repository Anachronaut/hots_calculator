from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.core import serializers
from .models import Hero
from .forms import AllySelectForm, OpponentSelectForm, AllyBanForm, OpponentBanForm
import json
from hots_calculator import settings


# #TODO: Implement sessions, cookies to stop using one set of global dicts for every user
# removed_form_key = {}
# removed_hero_key = {}

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





'''
Checks if select form selected option is already chosen
and if it is, whether or not it should be still recorded
as chosen. Pulls hero and matchup data, including images
and sends them back to the AJAX function in the homepage 
template
'''

def hero_update(request):
    hero_id = request.GET.get('hero', None)
    form_id = request.GET.get('formid', None)
    selected = False
    d={}

    if hero_id != '':
        hero = Hero.objects.filter(id=hero_id).values()
        #print('HERO:',hero)
        hero_img = hero[0]['image']
        hero_name = hero[0]['name']
        hero_winr = hero[0]['win_rate']
        hero_wins = hero[0]['win_total']
        hero_loss = hero[0]['loss_total']
        hero_gplay = hero[0]['games_played']
        
        for i,j in enumerate(range(5), 1):
            str_i = str(i)
            d["ally{0}".format(i)] = Hero.objects.filter(name=hero[0]['ally_'+str_i]).values()
            d["ally_img{0}".format(i)] = d["ally{0}".format(i)][0]['image']
            d["ally_name{0}".format(i)] = d["ally{0}".format(i)][0]['name']
            d["ally_win{0}".format(i)] = d["ally{0}".format(i)][0]['ally_'+str_i+'_win']

            d["enemy{0}".format(i)] = Hero.objects.filter(name=hero[0]['enemy_'+str_i]).values()
            d["enemy_img{0}".format(i)] = d["enemy{0}".format(i)][0]['image']
            d["enemy_name{0}".format(i)] = d["enemy{0}".format(i)][0]['name']
            d["enemy_win{0}".format(i)] = d["enemy{0}".format(i)][0]['enemy_'+str_i+'_win']

    removed_form_key = request.session.get('removed_form_key', {})
    removed_hero_key = request.session.get('removed_hero_key', {})

    if form_id in removed_form_key:                                        #Checks if select field has already been used
        form_hero = removed_form_key[form_id]                              #Sets previously selected hero from current select field
        if form_hero in removed_hero_key and form_id in removed_form_key:  #Check if previously selected hero is still recorded as selected
            del removed_hero_key[form_hero]                                #Removes previous hero when deselected
    
    if hero_id in removed_hero_key and form_id not in removed_form_key:    #Check if currently selected hero already selected by another select field
        selected = True
    elif hero_id in removed_hero_key and form_id in removed_form_key:      #Check if currently selected hero is registered as selected and if current select field has already been used
        if form_hero in removed_hero_key:                                  #Check if previously selected hero is still recorded as selected
            del removed_hero_key[form_hero] #Removes previous hero

        if hero_id in removed_form_key.values():                           #Check if currently selected hero selected by another select field
            selected = True
        else:                                                              #If not selected by another field, set current field's selection to selected hero
            removed_form_key[form_id] = hero_id

        if form_hero in removed_hero_key:                                  #Check if previously selected hero still registered as selected
            del removed_hero_key[form_hero] #Removes previous hero
        del removed_form_key[form_id] #Removes form's selected status
    
    elif hero_id == '': #Check if no hero, or "No Hero Selected" selected, set to empty values, default images
        hero_name = ''
        hero_winr = ''
        hero_wins = ''
        hero_loss = ''
        hero_gplay = ''
        hero_img = "hero_images/unk.png"

        for i,j in enumerate(range(5), 1):
            d["ally_img{0}".format(i)] = "hero_images/unk.png"
            d["ally_name{0}".format(i)] = ''
            d["ally_win{0}".format(i)] = ''

            d["enemy_img{0}".format(i)] = "hero_images/unk.png"
            d["enemy_name{0}".format(i)] = ''
            d["enemy_win{0}".format(i)] = ''


        form_hero = removed_form_key[form_id]
        if form_hero in removed_hero_key:       #Check if previously selected hero still registered as selected
            del removed_hero_key[form_hero]     #Removes previously selected hero
        del removed_form_key[form_id]           #Removes form's selected status

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
        'ally_img1': d['ally_img1'],
        'ally_name1': d['ally_name1'],
        'ally_win1': d['ally_win1'],
        'ally_img2': d['ally_img2'],
        'ally_name2': d['ally_name2'],
        'ally_win2': d['ally_win2'],
        'ally_img3': d['ally_img3'],
        'ally_name3': d['ally_name3'],
        'ally_win3': d['ally_win3'],
        'ally_img4': d['ally_img4'],
        'ally_name4': d['ally_name4'],
        'ally_win4': d['ally_win4'],
        'ally_img5': d['ally_img5'],
        'ally_name5': d['ally_name5'],
        'ally_win5': d['ally_win5'],
        'enemy_img1': d['enemy_img1'],
        'enemy_name1': d['enemy_name1'],
        'enemy_win1': d['enemy_win1'],
        'enemy_img2': d['enemy_img2'],
        'enemy_name2': d['enemy_name2'],
        'enemy_win2': d['enemy_win2'],
        'enemy_img3': d['enemy_img3'],
        'enemy_name3': d['enemy_name3'],
        'enemy_win3': d['enemy_win3'],
        'enemy_img4': d['enemy_img4'],
        'enemy_name4': d['enemy_name4'],
        'enemy_win4': d['enemy_win4'],
        'enemy_img5': d['enemy_img5'],
        'enemy_name5': d['enemy_name5'],
        'enemy_win5': d['enemy_win5']
    }

    request.session['removed_hero_key'] = removed_hero_key
    request.session['removed_form_key'] = removed_form_key

    return JsonResponse(data)





def reset(request): #Reset button, resets global dicts
    if (request.GET.get('reset-button')):
        request.session.pop('removed_form_key')
        request.session.pop('removed_hero_key')
    return redirect('homepage')
