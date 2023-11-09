from django.forms import ModelForm

from collegestore_app.models import Register


class RegisterForm(ModelForm):
    class Meta:

        model = Register
        fields = ["username", "password", "password1"]
