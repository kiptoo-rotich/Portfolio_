from django import forms
from django.forms.fields import ChoiceField
from .models import Project
class Technologies(forms.ModelForm):
    
    languages = forms.MultipleChoiceField(choices=ChoiceField, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Project
        fields = '__all__'