from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Brands, TrailCamPro, Supplier, Accessories

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def recruitment(request):
    return render(request, 'recruitment.html', {})


def support(request):
    return render(request, 'support.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def trailCam(request):
    brands = Brands.objects.all()
    trailCamPro = TrailCamPro.objects.all()
    classifiedProd = {}
    for i in trailCamPro:
        if i.brand_id not in classifiedProd:
            classifiedProd[i.brand_id] = []
        classifiedProd[i.brand_id].append(i)

    return render(request, 'trailCam.html', {'brands':brands, 'classifiedProd':classifiedProd, 'trailCamPro':trailCamPro})

# class TrailCam(ListView):
#     model = TrailCamPro

def trailCamPro(request, id):
    trailCamPro = TrailCamPro.objects.get(id = id)
    return render(request, 'trailCamPro.html', {'trailCamPro': trailCamPro})