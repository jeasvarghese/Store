from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ProfileForm
from .models import Department, Profile, Course


from .registerform import RegisterForm


# Create your views here.

def index(request):

    return  render(request,"index.html")
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username= username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('collegestore_app:newpage')
        else:
            messages.info(request,"invalid credentials")
            return redirect('collegestore_app:login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        details = RegisterForm(request.POST)
        if details.is_valid():
            username=request.POST['username']
            password = request.POST['password']
            cpassword=request.POST['password1']
            if password==cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username Taken")
                    return redirect('collegestore_app:register')
                else:
                    user=User.objects.create_user(username=username,password=password)
                    user.save();
                    return redirect('collegestore_app:login')
            else:
                messages.info(request,"password is not matching")
                return redirect('collegestore_app:register')
            return redirect('/')
        else:
            messages.info(request, "form not valid")
            return redirect('collegestore_app:register')
    return render(request,"register.html")



def logout(request):
    auth.logout(request)
    return render(request,"index.html")

# def profile(request):
#     dept = Department.objects.all()
#     if request.method  == 'POST':
#         details = ProfileForm(request.POST)
#         if details.is_valid():
#             name = request.POST['name']
#             age = request.POST['age']
#             dob = request.POST['dob']
#             phonenumber = request.POST['phone']
#             gender = request.POST['gender']
#             address = request.POST['address']
#             mailid = request.POST['email']
#             department = request.POST['department']
#             course = request.POST['course']
#             material = request.POST['material']
#             purpose = request.POST['purpose']
#
#             student = Profile.objects.create(NAME=name,DOB=dob,AGE=age,PHONE_NUMBER=phonenumber,
#                                               GENDER=gender,ADDRESS=address,MAIL_ID=mailid,
#                                               DEPARTMENT=dept.get(pk = department),
#                                               COURSE=course,MATERIAL=material,PURPOSE=purpose)
#             student.save()
#             messages.success(request,"Order Confirmed.")
#             return redirect('collegestore_app:profile')
#         else:
#             messages.info(request, "Form not valid")
#             return redirect('collegestore_app:profile')
#
#     context = {
#         'dept':dept,
#     }
#     return render(request, "profile.html",context)


# def profile(request):
#     dept = Department.objects.all()
#     if request.method  == 'POST':
#
#
#             name = request.POST['name']
#             age = request.POST['age']
#             dob = request.POST['dob']
#             phonenumber = request.POST['phone']
#             gender = request.POST['gender']
#             address = request.POST['address']
#             mailid = request.POST['email']
#             department = request.POST['department']
#             course = request.POST['courses']
#             material = request.POST['material']
#             purpose = request.POST['purpose']
#
#             student = Profile.objects.create(NAME=name,DOB=dob,AGE=age,PHONE_NUMBER=phonenumber,
#                                               GENDER=gender,ADDRESS=address,MAIL_ID=mailid,
#                                               DEPARTMENT=dept.get(pk = department),
#                                               COURSE=course,MATERIAL=material,PURPOSE=purpose)
#             student.save()
#             messages.success(request,"Order Confirmed.")
#             return redirect('collegestore_app:profile')
#
#     context = {
#         'dept':dept,
#     }
#     return render(request, "profile.html",context)
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order Confirmed')
            return redirect('collegestore_app:profile')
        else:
            messages.info(request, form.errors)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})

def newpage(request):
    return  render(request,"newpage.html")

# def load_courses(request):
#     department_id = request.GET.get('department_id')
#     courses = Course.objects.filter(department_id=department_id).all()
#     return render(request, 'dropdown.html', {'courses': courses})