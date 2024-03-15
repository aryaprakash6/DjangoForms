from django import forms
from django.core import validators


def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('start with a')

def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5')

def clean(self):
    e = self.cleaned_data['email']
    r = self.cleaned_data['reenteremail']
    if r!=e:
        raise forms.ValidationError('emails not matched')

class Schoolform(forms.Form):
    sname= forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(4)])
    Sprincipal=forms.CharField(validators=[validate_for_a])
    Slocation = forms.CharField()
    email= forms.EmailField()
    reenteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('Bot')

