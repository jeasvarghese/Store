from django.forms import ModelForm

from collegestore_app.models import Profile, Course


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email", "address","age","dob","phone","gender","departments","courses","purpose","material"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['COURSE'].queryset = Course.objects.none()
    #
    #     if 'DEPARTMENT' in self.data:
    #         try:
    #             department_id = int(self.data.get('DEPARTMENT'))
    #             self.fields['COURSE'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['COURSE'].queryset = self.instance.department.course_set.order_by('name')

