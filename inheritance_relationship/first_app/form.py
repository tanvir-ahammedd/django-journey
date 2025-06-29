from django import forms
from . models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # exclude = ['roll', 'name']
        # fields = ['roll', 'name']
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }