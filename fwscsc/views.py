from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Brands, Department, TrailCamPro, Supplier, Accessories, Recruitment, Department

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def recruitment(request):
    recruitment = Recruitment.objects.all()
    department = Department.objects.all()
    classifiedRec = {}
    for i in recruitment:
        if i.department not in classifiedRec.keys():
            classifiedRec[i.department] = []
        classifiedRec[i.department].append(i)
    return render(request, 'recruitment.html',
    {'recruitment':recruitment, 'department':department, 'classifiedRec':classifiedRec})


def support(request):
    return render(request, 'support.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def trailCam(request):
    brands = Brands.objects.all()
    trailCamPro = TrailCamPro.objects.all()
    classifiedProd = {}
    for i in trailCamPro:
        if i.brand not in classifiedProd.keys():
            classifiedProd[i.brand] = []
        classifiedProd[i.brand].append(i)

    return render(request, 'trailCam.html', {'brands':brands, 'classifiedProd':classifiedProd, 'trailCamPro':trailCamPro})

# class TrailCam(ListView):
#     model = TrailCamPro

def trailCamPro(request, id):
    trailCamPro = TrailCamPro.objects.get(id = id)
    return render(request, 'trailCamPro.html', {'trailCamPro': trailCamPro})


