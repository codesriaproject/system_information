from django import forms

from users.models import *



class DateInput(forms.DateInput):
    input_type = "date"



class AddStaffForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    salary=forms.CharField(label="Salary",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number=forms.CharField(label="Phone Number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    nationality=forms.CharField(label="Nationality",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    departments=Department.objects.all()
    department_list=[]
    for department in departments:
        small_department=(department.id,department.name)
        department_list.append(small_department)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others"),
    )


    status_choice=(
        ("chef","Chef"),
        ("employee","Employee"),
        ("secretaire","Secretaire"),
    )

    department=forms.ChoiceField(label="Department",choices=department_list,widget=forms.Select(attrs={"class":"form-control"}))
    gender=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    status=forms.ChoiceField(label="Status",choices=status_choice,widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))










class AddVigilForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number=forms.CharField(label="Phone Number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))

