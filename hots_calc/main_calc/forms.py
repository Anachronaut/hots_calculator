from django import forms
from django.forms import ModelForm
from .models import Hero

from django.forms import ValidationError


class AllySelectForm(forms.Form):
    ally_draft_pick = forms.ModelChoiceField(queryset=Hero.objects.all(), empty_label="Select an Allied Hero", widget=forms.Select(attrs={"onChange":'submit()'}))
    def __init__(self, *args, **kwargs):
        super(AllySelectForm, self).__init__(*args, **kwargs)
        self.fields['ally_draft_pick'].label = "Your Draft Pick"

class OpponentSelectForm(forms.Form):
    opp_draft_pick = forms.ModelChoiceField(queryset=Hero.objects.all(), empty_label="Select an Opponent Hero", widget=forms.Select(attrs={"onChange":'submit()'}))
    def __init__(self, *args, **kwargs):
        super(OpponentSelectForm, self).__init__(*args, **kwargs)
        self.fields['opp_draft_pick'].label = "Opponent Draft Pick"

class AllyBanForm(forms.Form):
    ally_ban = forms.ModelChoiceField(queryset=Hero.objects.all(), empty_label="Select a Hero to Ban", widget=forms.Select(attrs={"onChange":'submit()'}))
    def __init__(self, *args, **kwargs):
        super(AllyBanForm, self).__init__(*args, **kwargs)
        self.fields['ally_ban'].label = "Your Ban"

class OpponentBanForm(forms.Form):
    opp_ban = forms.ModelChoiceField(queryset=Hero.objects.all(), empty_label="Select a Hero to Ban", widget=forms.Select(attrs={"onChange":'submit()'}))
    def __init__(self, *args, **kwargs):
        super(OpponentBanForm, self).__init__(*args, **kwargs)
        self.fields['opp_ban'].label = "Opponent's Ban"