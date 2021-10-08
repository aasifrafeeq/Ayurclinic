from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import patients
from patients.models import *

# Create your views here.
def index(request):
    return render(request,"patients/index.html")

def patient(request,patient_id):
    patient=Patient.objects.get(pk=patient_id)
    meds=Medicine.objects.filter(users=patient)
    return render(request,"patients/details.html",{
        "patient":patient,
        "meds":meds,
    })

def med(request,med_id):
    medicine=Medicine.objects.get(pk=med_id)
    users=medicine.users.all()
    return render(request,"patients/details_med.html",{
        "users":users,
        "medicine":medicine
    })
def find_patient(request):
    patients=Patient.objects.all()
    if request.method=="POST":
        name=request.POST["patient"]
        result=Patient.objects.filter(name__contains=name)
        return render(request,"patients/find.html",{
            "title":"Find Patient",
            "results":result,
        })
    
    return render(request,"patients/find.html",{
        "title":"Find Patient",
    })

def find_users(request):
    if request.method=="POST":
        name=request.POST["medicine"]
        result=Medicine.objects.filter(name__contains=name)
        return render(request,"patients/find_med.html",{
            "results":result,
        })
    return render(request,"patients/find_med.html",{
        "title":"Find Users",
    })

def add(request):
    if request.method == "POST":
        #collecting data from form
        name=request.POST["name"]
        gender=request.POST["gender"]
        age=request.POST["age"]
        diagnosis=request.POST["diagnosis"]
        #saving data into db
        patient = Patient(name=name.upper(),gender=gender,age=age,diagnosis=diagnosis)
        patient.save()
        return HttpResponseRedirect(reverse('add_med',args=[patient.id]))
    return render(request,"patients/add.html")

def add_med(request,patient_id):
    patient=Patient.objects.get(id=patient_id)
    meds=patient.medicines.all()
    non_meds=Medicine.objects.exclude(users=patient).all()
    if request.method == "POST":
        medicine_name=request.POST["medicine"]
       # adding patient into the medicine user
        medicine=Medicine.objects.get(name=medicine_name)
        medicine.users.add(patient)
        new_meds=patient.medicines.all()
        new_non_meds=Medicine.objects.exclude(users=patient).all()
        return render(request,"patients/meds.html",{
        "patient":patient,
        "taking_meds":new_meds,
        "non_taking_meds":new_non_meds
        })
    return render(request,"patients/meds.html",{
        "patient":patient,
        "taking_meds":meds,
        "non_taking_meds":non_meds
    })
    return HttpResponseRedirect(reverse(index))
