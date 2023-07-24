from django.urls import path

from purchase import views
from django.conf.urls.static import static
from CodesriaSystem import settings

urlpatterns = [
    #=====================Demande urls Start===============================

    path('add_demande',views.add_demande, name="add_demande"),
    path('add_demande_save',views.add_demande_save, name="new_demande"),
    path('demande_list',views.demande_list,name="demande_list"),
    path('demande/add_purchase/<int:staffleav_id>', views.get_demande,name="commande"),
    path('demande/purchase/<int:demande_id>', views.demande_details, name='view'),
    #=====================Demande urls End===============================

    #=====================Purchase urls Start===============================    
    path('purchase_list',views.purchase_list,name="purchase_list"),
    # path('purchase_view/<int:id>', views.InvoiceView.as_view(), name='view_purchase'),
    path('purchase_view/<int:id>', views.InvoiceView.as_view(), name='view_purchase'),

    path('signature_view/', views.ModalView.as_view(), name='signature_view'),
    #=====================Fournisseur urls===============================


    #=====================Fournisseur urls Start===============================
    path('add_fournisseur',views.add_fournisseur, name="add_fournisseur"),
    path('add_fournisseur_save',views.add_fournisseur_save, name="new_client"),
    path('fournisseur_list',views.fournisseur_list,name="fournisseur_list"),

    #=====================Fournisseur urls End===============================

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)

