from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
    projets = models.Project.objects.filter(status=True)
    return render(request, 'index.html', locals())

@csrf_exempt
def post_donne(request):


    return JsonResponse(datas, safe=False)