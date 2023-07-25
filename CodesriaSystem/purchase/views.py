from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from purchase.forms import *
from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from purchase.models import *
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from purchase.sup import get_invoice
from users.models import *

# Create your views here.


#=================================Demande Start==================================

# @method_decorator(login_required(login_url='show_login'))
def add_demande(request):
    return render(request,"pages/staffPage/purchase_demande.html")



# @method_decorator(login_required(login_url='show_login'))
def add_demande_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddDemandeForm(request.POST,request.FILES)
        if form.is_valid():
            note_demande=form.cleaned_data["note_demande"]
            staff = get_object_or_404(Staff, admin_id=request.user.id)
            chef_recept=form.cleaned_data["chef_recept"]
            try:
                staffleave=StaffLeave(staff=staff,note_demande=note_demande)
                chef_recept_obj=Staff.objects.get(id=chef_recept)
                staffleave.chef_recept=chef_recept_obj
                staffleave.save()
                messages.success(request,"Successfully Added In Demande")
                return HttpResponseRedirect(reverse("add_demande"))
            except Exception as e:
                messages.error(request,"Failed to Add In Demande" + str(e))
                return HttpResponseRedirect(reverse("add_demande"))
        else:
            form=AddDemandeForm(request.POST)
            return render(request, "pages/staffPage/purchase_demande.html", {"form": form})

 

def demande_list(request):
    staff_instance = Staff.objects.get(admin_id=request.user)
    
    demande = StaffLeave.objects.filter(chef_recept_id= staff_instance).order_by('-date_demande')

    context = {
        'demande': demande,

    }
    return render(request,"pages/staffPage/demande_list.html", context)


def demande_details(request,demande_id):
    demande=StaffLeave.objects.get(id=demande_id)
    context={
        'demande':demande,
    }

    return render(request,"pages/staffPage/demande_details.html", context)


#=================================Demande End==================================



#=========================================Purchase Start=============================================






@transaction.atomic()
def get_demande(request,staffleav_id):
        staffleave=StaffLeave.objects.get(id=staffleav_id)
        customers = Fournisseur.objects.all()
        staff_instance = Staff.objects.get(admin_id=request.user)
        signatures = Signature.objects.filter(staff_sign_id=staff_instance)
        secretary_rept=Staff.objects.all()

        context = {
        'customers': customers,
        'staffleave':staffleave,
        'signatures':signatures,
        'secretary_rept':secretary_rept,
            }
        
        if request.method=="GET":
            return render(request, 'pages/staffPage/add_purchase.html', context)

        elif request.method=="POST":
        
            items = []

            try: 

                customer = request.POST.get('customer')
                
                signature = request.POST.get('signature')

                articles = request.POST.getlist('article')

                qties = request.POST.getlist('qty')

                units = request.POST.getlist('unit')

                total_a = request.POST.getlist('total-a')

                total = request.POST.get('total')

                observation = request.POST.get('observation')

                staffleave=request.POST.get("staffleave")

                secretary_rept=request.POST.get("secretary_rept")
                
                lieu_livraison = request.POST.get('lieu_livraison')

                invoice_object = {
                    'client_id': customer,
                    'signature_id': signature,
                    'staffleave_id':staffleave,
                    'secretary_recept_id':secretary_rept,
                    'total': total,
                    'lieu_livraison': lieu_livraison,
                    'observation': observation,
                    
                }

                invoice = Invoice.objects.create(**invoice_object)

                for index, article in enumerate(articles):

                    data = Article(
                        invoice_id = invoice.id,
                        name = article,
                        quantity=qties[index],
                        unit_price = units[index],
                        total = total_a[index],
                    )

                    items.append(data)

                created = Article.objects.bulk_create(items)   

                if created:
                    messages.success(request, "Purchase saved successfully.") 
                else:
                    messages.error(request, "Sorry, please try again the sent data is corrupt.")    

            except Exception as e:
                messages.error(request, f"Sorry the following error has occured {e}.")   

        return  render(request, 'pages/staffPage/add_purchase.html', context)



def purchase_list(request):
    staff_instance = Staff.objects.get(admin_id=request.user)
    
    invoice = Invoice.objects.filter(secretary_recept_id=staff_instance).order_by('-date_creation')

    context = {
        'invoice': invoice,

    }
    return render(request,"pages/staffPage/secretary_recept_purchase.html", context)


class InvoiceView(View):

    template_name = 'pages/staffPage/view_purchase.html'

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')
        context = get_invoice(id)

        return render(request, self.template_name, context)
    
    def post(self,request, *args, **kwargs):
        
        if request.method == 'POST':
            invoice_id=request.POST.get('id')
            signature = request.POST.get('signature')
            try:
                sign_secretary = SecretaryValidate()
                sign_secretary.purchase_recept_id=invoice_id
                sign_secretary.signature_id = signature
                sign_secretary.save()
                return HttpResponse(True)

            except Exception as e:
                return HttpResponse(False)

        return render(request,'pages/staffPage/view_purchase.html')



#=================================Purchase End==================================

#=================================Signature Secretary Start==================================


class ModalView(View):
    template_name="main/modal_sign.html"
    def get(self,request, *args, **kwargs):
        signature=Signature.objects.all()
        context={
                
                'signature':signature,
         
         }
        return render(request,self.template_name,context)



#=================================Signature Secretary End==================================

#=================================Fournisseur Start==================================


def add_fournisseur(request):
    return render(request,"pages/staffPage/add_fournisseur.html")



def add_fournisseur_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddFournisseurForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            address=form.cleaned_data["address"]
            phone_number=form.cleaned_data["phone_number"]
            try:
                founisseur=Fournisseur(name=name, address=address,phone_number=phone_number)
                founisseur.save()
                messages.success(request,"Successfully Added In Fournisseur")
                return HttpResponseRedirect(reverse("add_fournisseur"))
            except Exception as e:
                messages.error(request,"Failed to Add In Fournisseur" + str(e))
                return HttpResponseRedirect(reverse("add_fournisseur"))
        else:
            form=AddFournisseurForm(request.POST)
            return render(request, "pages/staffPage/add_fournisseur.html", {"form": form})



def fournisseur_list(request):
    
    fournisseur = Fournisseur.objects.all()

    context = {
        'fournisseur': fournisseur,

    }
    return render(request,"pages/staffPage/fournisseur_list.html", context)


#=================================Fournisseur End==================================
#=================================Voucher Start====================================

def get_voucher(request, staffleave_id):
        staffleave = StaffLeave.objects.get(id=staffleave_id)
        customers = Fournisseur.objects.all()
        staff_instance = Staff.objects.get(admin_id=request.user)
        signatures = Signature.objects.filter(staff_sign_id=staff_instance)
        secretary_recept = Staff.objects.all()

        context = {
            'customers': customers,
            'staffleave': staffleave,
            'signatures': signatures,
            'secretary_recept': secretary_recept,
        }

        if request.method == "GET":
            return render(request, 'pages/staffPage/add_voucher.html', context)

        elif request.method == "POST":

            try:

                customer = request.POST.get('customer')

                signature = request.POST.get('signature')

                chequetransfert = request.POST.get('chequetransfert')

                bankname = request.POST.get('bankname')

                budgetyear = request.POST.get('budgetyear')

                programmetype = request.POST.get('programmetype')

                programmecode = request.POST.get('programmecode')

                subprogrammecode = request.POST.get('subprogrammecode')

                programmeactivecode= request.POST.get('programmeactivecode')

                programmeactivetitle = request.POST.get('programmeactivetitle')

                donor=request.POST.get('donor')

                accountdebit=request.POST.get('accountdebit')

                accountcredit=request.POST.get('accountcredit')

                total = request.POST.get('total')

                description = request.POST.get('description')

                staffleave = request.POST.get("staffleave")

                secretary_recept = request.POST.get("secretary_recept")

                lieu_livraison = request.POST.get('lieu_livraison')

                invoice_object = {
                    'client_id': customer,
                    'signature_id': signature,
                    'staffleave_id': staffleave,
                    'secretary_recept_id': secretary_recept,
                    'total': total,
                    'lieu_livraison': lieu_livraison,
                    'description': description,
                    'chequetransfert':chequetransfert,
                    'bankname':bankname,
                    'budgetyear':budgetyear,
                    'programmetype':programmetype,
                    'programmeactivecode':programmeactivecode,
                    'subprogrammecode':subprogrammecode,
                    'programmecode':programmecode,
                    'programmeactivetitle':programmeactivetitle,
                    'donor':donor,
                    'accountdebit':accountdebit,
                    'accountcredit':accountcredit


                }

                created = Voucher.objects.create(**invoice_object)


                if created:
                    messages.success(request, "Voucher saved successfully.")
                else:
                    messages.error(request, "Sorry, please try again the sent data is corrupt.")

            except Exception as e:
                messages.error(request, f"Sorry the following error has occured {e}.")

        return render(request, 'pages/staffPage/add_voucher.html', context)


def voucher_list(request):
    staff_instance = Staff.objects.get(admin_id=request.user)
    voucher = Voucher.objects.filter(secretary_recept_id=staff_instance).order_by('-date_prepared')

    context = {
        'voucher': voucher,

    }
    return render(request, "pages/staffPage/voucher_list.html", context)


def voucher_details(request,voucher_id):
    voucher=Voucher.objects.get(id=voucher_id)
    context={
        'voucher':voucher,
    }

    return render(request,"pages/staffPage/view_voucher.html", context)