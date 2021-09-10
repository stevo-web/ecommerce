from django import forms
from Kenya.counties import counties
from main.models import Category

county_choices = [(f'{county["name"]}', f'{county["name"]}') for county in counties]
county_choices = tuple(county_choices)

sale_choices = tuple([(f'{cat.name}', f'{cat.name}') for cat in Category.objects.all()])


class CreateShop(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.ChoiceField(choices=county_choices, widget=forms.Select(attrs={
        'class': 'custom-select d-block w-100'
    }))
    sale = forms.ChoiceField(choices=sale_choices, widget=forms.RadioSelect(attrs={
        "class": ""
    }))
    mpesa_till = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))


