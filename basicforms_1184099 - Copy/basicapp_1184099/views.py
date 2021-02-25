from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'basicapp_1184099/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("--------Validation Success--------")
            print("NAME         : "+form.cleaned_data['nama_depan']+" "+form.cleaned_data['nama_belakang'])
            print("JENIS KELAMIN: "+form.cleaned_data['jenis_kelamin'])
            print("EMAIL        : "+form.cleaned_data['email'])
            print("TEXT         : "+form.cleaned_data['text'])

    return render(request,'basicapp_1184099/form_page.html', {'form':form})
