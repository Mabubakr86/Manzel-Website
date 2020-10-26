from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Property(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    desc = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='properties/', null=True)
    location = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'



    def save(self,*args,**kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Property, self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name

class PropertyImages(models.Model):
    _property = models.ForeignKey(to=Property, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='properties/images/', null=True)


class PropertyRating(models.Model):
    _property = models.ForeignKey(to=Property, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name