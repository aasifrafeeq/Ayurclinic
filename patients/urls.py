from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("find_patient/",views.find_patient,name="find_patient"),
    path("add/",views.add,name="add"),
    path("patient/<int:patient_id>",views.patient,name="patient"),
    path("add_med/<int:patient_id>",views.add_med,name="add_med"),
    path("find_users/",views.find_users,name="find_users"),
    path("med/<int:med_id>",views.med,name="med")
]