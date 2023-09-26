from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("<int:month>", views.mon_chall_num),
    path("<str:month>", views.mon_chall,name="monthly_chal")
]