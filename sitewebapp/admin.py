from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models
# Register your models here.

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titre', 'bienvenue_message', 'image', 'status')

    # def image_view(self, obj):
    #     return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px" >')



@admin.register(models.Animation)
class AnimationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'status')




@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'annee','status')



@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'annee','status')



@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'icon', 'link', 'status')


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('nom', 'image_view', 'date_add', 'status')

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px" >')



@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('nom_site', 'phone', 'email', 'status')



@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('entete_projet', 'entete_contact', 'date_add', 'status')
