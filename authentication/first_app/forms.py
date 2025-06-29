from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django import forms

class NoHelpTextMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        exceptions = getattr(self, 'help_text_exceptions', [])
        for name, field in self.fields.items():
            if name not in exceptions:
                field.help_text = ''
          
class RegisterForm(NoHelpTextMixin, UserCreationForm):
    help_text_exceptions = ['password']   # Fields that should keep their help text
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
                       
class ChangeUserData(NoHelpTextMixin, UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']      

class CustomPasswordChangeForm(NoHelpTextMixin,PasswordChangeForm):
    pass

class CustomSetPasswordForm(NoHelpTextMixin,SetPasswordForm):
    pass
