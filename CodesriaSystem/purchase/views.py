from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from purchase.forms import *
from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from purchase.models import *
from django.db import transaction
from django.views import View
from purchase.sup import get_invoice

# Create your views here.

# @method_decorator(login_required(login_url='show_login'))
def add_demande(request):
    return render(request,"pages/staffPage/purchase_demande.html")


# @method_decorator(login_required(login_url='show_login'))
def add_demande_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddDemandeForm(request.POST)
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
    
    demande = StaffLeave.objects.all().order_by('-date_demande')

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


#=========================================PURCHASE=============================================






@transaction.atomic()
def get_demande(request,staffleav_id):
        staffleave=StaffLeave.objects.get(id=staffleav_id)
        customers = Fournisseur.objects.all()

        context = {
        'customers': customers,
        'staffleave':staffleave
            }


        
        if request.method=="GET":
            return render(request, 'pages/staffPage/add_purchase.html', context)

        elif request.method=="POST":
        
            items = []

            try: 

                customer = request.POST.get('customer')

                articles = request.POST.getlist('article')

                qties = request.POST.getlist('qty')

                units = request.POST.getlist('unit')

                total_a = request.POST.getlist('total-a')

                total = request.POST.get('total')

                observation = request.POST.get('observation')

                staffleave=request.POST.get("staffleave")
                
                lieu_livraison = request.POST.get('lieu_livraison')

                invoice_object = {
                    'client_id': customer,
                    'staffleave_id':staffleave,
                    'total': total,
                    'lieu_livraison': lieu_livraison,
                    'observation': observation
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
    
    invoice = Invoice.objects.all().order_by('-date_creation')

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
