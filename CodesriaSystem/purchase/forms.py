from django import forms
from ckeditor.widgets import CKEditorWidget
from purchase.models import *
from users.models import *





class AddDemandeForm(forms.Form):
    note_demande =forms.CharField(widget=CKEditorWidget(),required=True)


    

    chef_recepts=Staff.objects.filter(department_id=1, status="chef")
    staff_list=[]
    for staff in chef_recepts:
        small_staffs=(staff.id,staff.admin.first_name)
        staff_list.append(small_staffs)
    chef_recept=forms.ChoiceField(label="Staff Recept",choices=staff_list,widget=forms.Select(attrs={"class":"form-control"}),required=True)


    signatures=Signature.objects.all()
    signature_list=[]
    for signature in signatures:
        small_signature=(signature.id,signature.sign)
        signature_list.append(small_signature)

    signature=forms.ChoiceField(label="Signature",choices=signature_list,widget=forms.Select(attrs={"class":"form-control"}),required=True)





class AddSignForm(forms.Form):

    signatures=Signature.objects.all()
    signature_list=[]
    for signature in signatures:
        small_signature=(signature.id,signature.sign)
        signature_list.append(small_signature)


    signature=forms.ChoiceField(label="Signature",choices=signature_list,widget=forms.Select(attrs={"class":"form-control"}),required=True)
    





class AddFournisseurForm(forms.Form):
    name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number=forms.CharField(label="Phone Number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

