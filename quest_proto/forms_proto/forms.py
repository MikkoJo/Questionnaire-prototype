from django import forms

class questForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    
    