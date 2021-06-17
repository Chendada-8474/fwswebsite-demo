from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import TrailCamBrand, Department, TrailCamPro, Supplier, Accessories, Recruitment, Department

# Create your views here.

def home(request):
    trailCamBrand = TrailCamBrand.objects.all()
    return render(request, 'home.html', {'trailCamBrand':trailCamBrand, })


def about(request):
    trailCamBrand = TrailCamBrand.objects.all()
    return render(request, 'about.html', {'trailCamBrand':trailCamBrand, })


def recruitment(request):
    trailCamBrand = TrailCamBrand.objects.all()
    recruitment = Recruitment.objects.all()
    department = Department.objects.all()
    classifiedRec = {}
    for i in recruitment:
        if i.department not in classifiedRec.keys():
            classifiedRec[i.department] = []
        classifiedRec[i.department].append(i)
    return render(request, 'recruitment.html',
    {'trailCamBrand':trailCamBrand, 'recruitment':recruitment, 'department':department, 'classifiedRec':classifiedRec})


def support(request):
    trailCamBrand = TrailCamBrand.objects.all()
    return render(request, 'support.html', {'trailCamBrand':trailCamBrand, })


def contact(request):
    trailCamBrand = TrailCamBrand.objects.all()
    return render(request, 'contact.html', {'trailCamBrand':trailCamBrand, })




def trailCam(request):
    trailCamBrand = TrailCamBrand.objects.all()
    trailCamPro = TrailCamPro.objects.all()
    classifiedProd = {}
    for i in trailCamPro:
        if i.brand not in classifiedProd.keys():
            classifiedProd[i.brand] = []
        classifiedProd[i.brand].append(i)

    return render(request, 'trailCam.html', {'trailCamBrand':trailCamBrand, 'classifiedProd':classifiedProd, 'trailCamPro':trailCamPro})

# class TrailCam(ListView):
#     model = TrailCamPro

def trailCamPro(request, id):
    trailCamBrand = TrailCamBrand.objects.all()
    trailCamPro = TrailCamPro.objects.get(id = id)
    return render(request, 'trailCamPro.html', {'trailCamBrand':trailCamBrand, 'trailCamPro': trailCamPro})


