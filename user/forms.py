from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name',]

class PersonalDataForm(forms.Form):
   first_name = forms.CharField(required=True, max_length=255)
   last_name = forms.CharField(required=True, max_length=255)
   email = forms.EmailField(required=True)
   phone = forms.CharField(required=True, max_length=200)
   address = forms.CharField(max_length=1000, widget=forms.Textarea())