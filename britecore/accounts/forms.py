from django import forms
from .models import Risk

RType = [
    ("Automobile Policy", "Automobile Policy"),
    ("Cyber Liability Coverage", "Cyber Liability Coverage"),
    ("Prize Insurance", "Prize Insurance")
]

CType = [
    ("USD", "USD"),
    ("CAD", "CAD"),
    ("EUR", "EUR")
]

class HomeForm(forms.ModelForm):
    risk_type = forms.CharField(label='What is your Insurance type', widget=forms.Select(choices=RType))
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()
    zipCode = forms.IntegerField()
    prize_amount = forms.IntegerField()
    currency = forms.CharField(label='Choose your currency', widget=forms.Select(choices=CType))

    class Meta:
        model = Risk
        fields = '__all__'
