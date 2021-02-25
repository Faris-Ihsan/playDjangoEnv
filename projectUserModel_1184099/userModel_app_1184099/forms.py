from django import forms
from userModel_app_1184099.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'