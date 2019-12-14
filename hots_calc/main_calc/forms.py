from django import forms
from django.forms import ModelForm
from .models import Hero

from django.forms import ValidationError


class AllySelectForm(forms.Form):
    a_draft = forms.ModelChoiceField(queryset=Hero.objects.all().order_by('popularity').reverse(), empty_label="No Hero Selected")
    def __init__(self, *args, **kwargs):
        super(AllySelectForm, self).__init__(*args, **kwargs)
        self.fields['a_draft'].label = "Your Draft Pick"
        self.fields['a_draft'].widget.attrs['class'] = 'select_form'

class OpponentSelectForm(forms.Form):
    o_draft = forms.ModelChoiceField(queryset=Hero.objects.all().order_by('popularity').reverse(), empty_label="No Hero Selected")
    def __init__(self, *args, **kwargs):
        super(OpponentSelectForm, self).__init__(*args, **kwargs)
        self.fields['o_draft'].label = "Opponent Draft Pick"
        self.fields['o_draft'].widget.attrs['class'] = 'select_form'

class AllyBanForm(forms.Form):
    a_ban = forms.ModelChoiceField(queryset=Hero.objects.all().order_by('popularity').reverse(), empty_label="No Hero Selected")
    def __init__(self, *args, **kwargs):
        super(AllyBanForm, self).__init__(*args, **kwargs)
        self.fields['a_ban'].label = "Your Ban"
        self.fields['a_ban'].widget.attrs['class'] = 'select_form'

class OpponentBanForm(forms.Form):
    o_ban = forms.ModelChoiceField(queryset=Hero.objects.all().order_by('popularity').reverse(), empty_label="No Hero Selected")
    def __init__(self, *args, **kwargs):
        super(OpponentBanForm, self).__init__(*args, **kwargs)
        self.fields['o_ban'].label = "Opponent's Ban"
        self.fields['o_ban'].widget.attrs['class'] = 'select_form'