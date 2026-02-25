from django.shortcuts import render, redirect 
from .models import Student 

# Create your views here.
def home(request):
    return render(request, 'student_info/index.html')

def add_student(request):
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mail = request.POST.get('email')
        birth = request.POST.get('dob')
        sex = request.POST.get('gender')
        profile_pic = request.POST.get('image')
        s_country = request.POST.get('country')
        msg = request.POST.get('message')
        
        Student.objects.create(
            first_name = firstname,
            last_name = lastname,
            email = mail,
            dob = birth,
            gender = sex,
            pro_pic = profile_pic,
            country = s_country,
            message = msg 
        )
        
        return redirect(all_students)
    
    return render(request,'student_info/add_student.html')

def all_students(request):
    
    student_data = Student.objects.all()
    
    context_dict = {
        'data' : student_data
    }
    
    return render(request, 'student_info/all_students.html', context_dict)

def about(request):
    return render(request, 'student_info/about.html')



