from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(max_length=4, primary_key=True)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Roll: {self.roll} - {self.name}"