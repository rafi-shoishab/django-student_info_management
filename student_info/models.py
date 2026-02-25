from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    gender = models.CharField()
    pro_pic = models.ImageField(upload_to='student_img/', null=True, blank=True)
    country = models.CharField()
    message = models.TextField(max_length=200)