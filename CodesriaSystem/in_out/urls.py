from django.urls import path
from in_out import views


urlpatterns = [
    path('enter_list',views.list_vigil_enter,name="enter_list"),
    path('exit_list',views.list_vigil_exit,name="exit_list"),

    
]
