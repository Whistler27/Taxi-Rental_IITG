from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . models import Contact
from django.urls import reverse
from taxi.helper import get_user
from taxi.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token


def index(request):
    return render(request,'taxi/index.html')

def info(request):
    return render(request,'taxi/info.html')

def dashboard(request):
    return render(request,'taxi/dashboard.html')

def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get("Email")
        message = request.POST.get("Message")
        contact = Contact(name = name,email = email,message = message)
        contact.save()
        thank = True
    return render(request, 'taxi/contact.html', {'thank': thank})

def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

  # Get the user's profile
  user = get_user(token)

  # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect(reverse('taxi/'))