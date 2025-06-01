from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField 
from .models import User

class UserForm(forms.ModelForm):
      name = forms.CharField(
            label="Usuário" , widget=forms.TextInput())
      email = forms.EmailField(
            label="Email" , widget=forms.TextInput())
      day_of_birth = forms.DateField(
            label = "Data de nascimento", widget=forms.DateInput())
      password = forms.CharField( 
          label="Senha" , widget=forms.PasswordInput())

      
      class Meta:
        model = User
        fields = ['name'  ,'email' , 'day_of_birth', 'password']
