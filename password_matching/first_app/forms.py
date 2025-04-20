from django import forms
from django.core import validators
    
class PasswordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        
        if len(val_name) < 10:
            raise forms.ValidationError('Must be 10 character')
        if val_pass != val_conpass:
            raise forms.ValidationError('Password doesnt match')
        
    