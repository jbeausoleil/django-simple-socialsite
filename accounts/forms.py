from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from . import models

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].labels = 'Display Name'     # Acts in place of HTML label
            self.fields['email'].labels = 'Email Address'       # Acts in place of HTML label