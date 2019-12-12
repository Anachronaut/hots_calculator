from django import forms
from django.forms import ModelForm
from .models import Hero

from django.forms import ValidationError

'''
class HeroSelectForm(forms.Form):
    heroes = forms.ModelChoiceField(queryset=Hero.objects.all(), widget=forms.Select)
    def __init__(self, *args, **kwargs):
        super(HeroSelectForm, self).__init__(*args, **kwargs)
        self.fields['id'].queryset = Hero.objects.all()
'''
#print(Hero.objects.all())