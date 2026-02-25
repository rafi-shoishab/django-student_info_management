from django.contrib import admin 
from .models import Student 

# Register your models here.
@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin): 
    list_display = ('id', 'first_name', 'email', 'gender', 'pro_pic', 'country') 
    search_fields = ('id',) 
    list_filter = ('gender', 'country') 
    ordering = ('id',) 