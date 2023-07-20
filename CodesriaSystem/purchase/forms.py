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
