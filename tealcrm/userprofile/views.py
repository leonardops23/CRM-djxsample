from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Userprofile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a Userprofile instance for the new user
            # This assumes you have a Userprofile model that has a one-to-one relationship with the User model
            # If you have additional fields in Userprofile, you can set them here as well
            # For example: userprofile = Userprofile(user=user, additional_field=value)
            # Assuming Userprofile has a one-to-one relationship with User
            userprofile = Userprofile(user=user) 

            return redirect('/log-in/')  # Redirect to login after signup

    form = UserCreationForm()
    return render(request, 'userprofile/sign_up.html', {'form': form})
