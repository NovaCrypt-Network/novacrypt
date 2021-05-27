from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Chapter(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    reigon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    president = models.CharField(max_length=100)
    email = models.EmailField()
    instagram = models.URLField(blank=True)
    website = models.URLField(blank=True)
    def __str__(self):
        return f"Chapter {self.name} in {self.reigon}, {self.country.name}. Run by {self.president}."