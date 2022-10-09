from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserregistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password1']