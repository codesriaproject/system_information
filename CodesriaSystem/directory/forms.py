from django import forms
from django_countries.fields import CountryField
from directory.models import *



class AddStatusForm(forms.Form):
    name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))



class AddDirectoryForm(forms.Form):
    name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    surname =forms.CharField(label="Surname",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    countries=CountryField().formfield(widget=forms.Select(attrs={'class': 'form-control'}))
    email=forms.CharField(label="Email",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    phone_number=forms.CharField(label="Phone Number",widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    biography=forms.CharField(label="Biography",widget=forms.Textarea(attrs={"class":"form-control"}),required=False)
    bibliography=forms.CharField(label="Bibliography",widget=forms.Textarea(attrs={"class":"form-control"}),required=False)
    orcid=forms.CharField(label="Orcid",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    affliation=forms.CharField(label="Affliation",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

    statuss=Status.objects.all()
    status_list=[]
    for stat in statuss:
        small_status=(stat.id,stat.name)
        status_list.append(small_status)


    gender_choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others"),
    )    


    status=forms.ChoiceField(label="Status",choices=status_list,widget=forms.Select(attrs={"class":"form-control"}))
    
    gender=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
