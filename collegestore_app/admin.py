from django.contrib import admin
from .models import Profile, Department, Course

# Register your models here.
admin.site.register(Profile)
# admin.site.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ['name']
# admin.site.register(Department,DepartmentAdmin)
# admin.site.register(Course)