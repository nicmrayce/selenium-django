from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from loadselenium.utils import generate_token

# Create your views here.
def generate(requests):
    if requests.method == 'POST' and 'run_script' in requests.POST:

        # import function to run

        # call function
        generate_token()
        print('FB token is successfully generated')

        # return user to required page
        return HttpResponseRedirect(reverse('generate'))

    return render(requests, 'generate.html')