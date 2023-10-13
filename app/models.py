from django.db import models

# Create your models here.
from django.urls import reverse

class College(models.Model):
    Cname=models.CharField(max_length=100)
    Cprincipal=models.CharField(max_length=100)
    Clocation=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.Cname
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    

class Teacher(models.Model):
    Tname=models.CharField(max_length=100)
    Tage=models.IntegerField()
    Cname=models.ForeignKey(College,on_delete=models.CASCADE,related_name='teachers')

    def __str__(self) -> str:
        return self.Tname

    




