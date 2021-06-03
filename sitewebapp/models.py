from django.db import models

# Create your models here.

class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        abstract = True

class Banner(Base):
    titre = models.CharField( max_length=250)
    bienvenue_message = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(upload_to='image_banner')

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
class Animation(Base):
    nom = models.CharField(max_length=250)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Animation Banner'
        verbose_name_plural = 'Animation Banners'



class Experience(Base):
    titre = models.CharField( max_length=250)
    annee = models.IntegerField()
    description = models.TextField()
    

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'



class Education(Base):
    titre = models.CharField( max_length=250)
    annee = models.IntegerField()
    description = models.TextField()
    

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Social(Base):
    nom = models.CharField( max_length=250)
    icon = models.CharField( max_length=250)
    link = models.URLField()
    

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

class Project(Base):
    nom = models.CharField( max_length=250)
    image = models.FileField( upload_to='image_project')

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
    



class Website(Base):
    nom_site = models.CharField( max_length=250)
    copy_right = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    email = models.EmailField()
    maps = models.TextField()
   
    def __str__(self):
        return self.nom_site

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'




class Configuration(Base):
    entete_projet = models.TextField()
    entete_contact = models.TextField()

    def __str__(self):
        return self.entete_projet

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'


class Contact(Base):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.entete_projet

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

