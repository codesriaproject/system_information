from django.urls import path
from django.conf.urls.static import static
from CodesriaSystem import settings


from users import views, StaffViews, HodViews, VigilView
urlpatterns = [
    path('',views.LoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('logout_user',views.logout_user,name="logout"),
    path("admin", HodViews.adminhome, name="admin_home"),
    

#=========================End Main===============================================
#=========================Start Staff===============================================

    path("staff", StaffViews.staffhome, name="staff_home"),
    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('staff/profil',StaffViews.staff_profilview,name="profil_staff"),
    path('staff_list',HodViews.list_staff,name="staff_list"),
    
#=========================End Staff===============================================
#=========================Start Vigil===============================================



    path("vigil", VigilView.vigilhome, name="vigil_home"),
    path('add_vigil',HodViews.add_vigil,name="add_vigil"),
    path('add_vigil_save',HodViews.add_vigil_save,name="add_vigil_save"),
    path("vigil/profil/", VigilView.vigil_profilview,name='profil_vigil'),
    path('vigil_list',HodViews.list_vigil,name="vigil_list"),
#=========================End Vigil===============================================
#=========================Start Vigil===============================================
     
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
