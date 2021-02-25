from django import forms
from django.core import validators
from captcha.fields import CaptchaField

def check_for_z(value):
   if value[0].lower() != 'z':
       raise forms.ValidationError("Nama harus dimulai menggunakan huruf Z")

def check_for_k(value):
    if value[-1].lower() != 'k':
        raise forms.ValidationError("Nama Harus Diakhiri menggunakan huruf k")
    

class FormName(forms.Form):
    nama_depan      = forms.CharField(validators=[check_for_z])
    nama_belakang   = forms.CharField(validators=[check_for_k])
    jenis_kelamin   = forms.ChoiceField(widget=forms.RadioSelect, choices=[('Perempuan', 'Perempuan'), ('Laki-Laki', 'Laki-Laki')])
    email           = forms.EmailField()
    verify_email    = forms.EmailField(label ='Enter your email again 1184099')
    text            = forms.CharField(widget=forms.Textarea)
    captcha         = CaptchaField()

    #method untuk menghapus isi forms
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        #melakukan validator email harus sama
        if email != vmail:
            raise forms.ValidationError("MAKE SURE YOUR EMAIL MATCH ")