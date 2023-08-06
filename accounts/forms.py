from django.contrib.auth.forms import(
                      UserCreationForm,
                       UserChangeForm)
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
   # The `Meta` class extends the `UserCreationForm` class and adds additional fields for a
   # `CustomUser` model.
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            
            "name",
            "date_engaged",
            "date_of_birth",
            "role",)
        
# The class CustomUserChangeForm is a subclass of UserChangeForm and specifies the model and fields to
# be used for the form.
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields 