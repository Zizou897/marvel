from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name= 'index'),
    path('post-data/', views.post_donne, name= 'post_data'),
]