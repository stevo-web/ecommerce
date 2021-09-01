from django import forms
from Kenya.counties import counties

counties_choices = [(f'{county["name"]}', f'{county["name"]}') for county in counties]
counties_choices.insert(0, ('none', 'select county'))
counties_choices = tuple(counties_choices)

payment_choices = (
    ('mpesa', 'M-pesa'),
    ('credit', 'Credit Card')
)


class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    county = forms.ChoiceField(widget=forms.Select(attrs={'class': 'custom-select d-block w-80 form-control'}),
                               choices=counties_choices)
    payment = forms.ChoiceField(widget=forms.RadioSelect, choices=payment_choices)
