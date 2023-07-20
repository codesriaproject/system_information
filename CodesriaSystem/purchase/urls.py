from django.urls import path

from purchase import views

urlpatterns = [
    path('add_demande',views.add_demande, name="add_demande"),
    path('add_demande_save',views.add_demande_save, name="new_demande"),
    path('demande_list',views.demande_list,name="demande_list"),
    path('demande/add_purchase/<int:staffleav_id>', views.get_demande,name="commande"),
    path('demande/purchase/<int:demande_id>', views.demande_details, name='view'),
    path('purchase_list',views.purchase_list,name="purchase_list"),
    path('purchase_view/<int:id>', views.InvoiceView.as_view(), name='view_purchase'),


]
