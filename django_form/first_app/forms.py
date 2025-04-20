from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # appointment = forms.DateTimeField()
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     def clean_name(self):
#         valname = self.cleaned_data['name']
#         if len(valname) < 10:
#             raise forms.ValidationError('Name must be at least 10 characters long.')
#         return valname
#     def clean_email(self):
#         valemail = self.cleaned_data['email']
#         if '.com' not in valemail:
#             raise forms.ValidationError('Must contains .com')
#         return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('At least 10 character')
        
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Must contain .com')

def lencheck(value):
    if len(value) < 10:
        raise forms.ValidationError('Enter at least 10 character')
    
class StudentData(forms.Form):
    name = forms.CharField(
        validators=[validators.MinLengthValidator(10, message='At least 10 characters')]
    )
    text = forms.CharField(widget=forms.TextInput, validators=[lencheck]) # use our own function
    email = forms.CharField(
        widget=forms.EmailInput,
        validators=[validators.EmailValidator(message='Enter a valid email')]
    )
    age = forms.IntegerField(
        validators=[
            validators.MaxValueValidator(34, message='Age must be at most 34'),
            validators.MinValueValidator(24, message='At least 24')  # corrected value/message
        ]
    )
    file = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],
                                                      message='File must be a .pdf')]
    )