from django.db import models

class SuperUser(models.Model):
    name = models.CharField(max_length=10,blank=False)
    surname = models.CharField(max_length=20, blank=False)
    faculty = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(default=16)
    def __str__(self):
        return f' {self.name} {self.surname}  винний 100 грн' \
               f''
# Create your models here.
