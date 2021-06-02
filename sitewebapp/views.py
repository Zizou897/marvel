from django.shortcuts import render

from . import models 
# Create your views here.


def index(request):
    banners = models.Banner.objects.filter(status=True).first()
    animations = models.Animation.objects.filter(status=True)
    experiences = models.Experience.objects.filter(status=True)
    educations = models.Education.objects.filter(status=True)
    sociaux = models.Social.objects.filter(status=True)
    confi = models.Configuration.objects.filter(status=True).first()
    site = models.Website.objects.filter(status=True).first()
    return render(request, 'index.html', locals())