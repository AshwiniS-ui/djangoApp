
from django.db import models

# Create your models here.
class student(models.Model):
    userId = models.IntegerField(max_length=45)
    name = models.CharField(max_length=35)
    department = models.CharField(max_length=45)
    cgpa = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return self.userId+'-'+self.name+'-'+self.department+'-'+self.cgpa

