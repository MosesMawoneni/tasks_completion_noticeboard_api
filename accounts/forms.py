from django.contrib.auth.forms import(
                      UserCreationForm,
                       UserChangeForm)
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "date_engaged",
            "date_of_birth",
            "role")
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields 