from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Departments,Doctors
from Home.forms import BookingForm
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)
def contacts(request):
    return render(request,'contacts.html')
def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)