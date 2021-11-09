from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='movie/actor/images',null=True,blank=True)
    id_name = models.OneToOneField("Idnumber",on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('-first_name',)
        verbose_name = 'Cast'

class Idnumber(models.Model):
    number = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.number

class Categories(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Categories'


class Review(models.Model):
    comment = models.TextField()
    attachment = models.FileField(upload_to='movie/attachment/review',null=True,blank=True)
    movie=models.ForeignKey("Movie",on_delete=models.SET_NULL,null=True)
    # user = models.FileField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE())

    def __str__(self):
       return "{} - Review ".format(self.movie.name)


class Movie(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField("Movie Name", unique=True, max_length=255)
    description = models.TextField(verbose_name="Movie Description")
    likes = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)
    rate = models.PositiveIntegerField(default=0)
    production_date = models.DateField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    actor = models.ManyToManyField(Actor)

    # comments
    poster = models.ImageField(upload_to='movie/movie/images')
    video = models.FileField(upload_to='movie/movie/videos')

    def __str__(self):
        return self.name
