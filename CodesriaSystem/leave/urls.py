from django.urls import path



# from django.urls import path, re_path
# from .views import ViewsToBeImported
from leave import views

# app_name = AppName

urlpatterns = [
    path("", views.testindex)
]