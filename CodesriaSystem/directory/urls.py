from django.urls import path
from directory import views

urlpatterns = [
    
    path('add_status',views.add_status,name="add_status"),
    path("new_status",views.add_status_save, name="new_status"),

    path('add_directory',views.add_directory,name="add_directory"),
    path("new_directory",views.add_directory_save, name="new_directory"),
    path('directory_list',views.list_directory,name="directory_list"),
    path('directory/members/<int:directory_id>', views.directory_details, name='directory_details'),

]
