from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=200)
    departments=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Department(models.Model):
#     department=models.ForeignKey(Department,on_delete=models.CASCADE)
#     course = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.department
#         return self.course
#
# class Course(models.Model):
#     name=models.CharField(max_length=200)
#
#
#     def __str__(self):
#         return self.name



class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField(max_length=1000)
    age = models.IntegerField()
    dob = models.DateField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=255)
    departments = models.CharField(max_length=255,null=True)
    courses = models.CharField(max_length=255,null=True)
    purpose = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Register(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password1 = models.CharField(max_length=255)
