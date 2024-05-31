from django.contrib.auth.backends import ModelBackend
from .models import Alumni

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the user exists with the provided username
            user = Alumni.objects.get(username=username)
        except Alumni.DoesNotExist:
            # If the user doesn't exist with the provided username, try with registration_no
            try:
                user = Alumni.objects.get(registration_no=username)
            except Alumni.DoesNotExist:
                # If the user doesn't exist with either username or registration_no, return None
                return None
        
        # If the user is found, check the password
        if user.check_password(password):
            return user  # Return the user object if authentication succeeds
        else:
            return None  # Return None if authentication fails