from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm


def index(request):

    return render(request,'index.html')



# def hello(request):

#     return HttpResponse(f"""
#         <h1>Hello Django from container!</h1>
# """)


# def homepage(request):
#     return render(request, 'myapp/homepage.html')

#########################################################

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Authentifier l'utilisateur nouvellement créé
            return redirect('home')  # Rediriger vers la page d'accueil après la création de compte
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
#####################################################################
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth_login(request, user)  # Utilisez la fonction auth_login pour éviter le conflit
                return redirect('home')
            else:
                # Gérer le cas où l'authentification échoue
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
#########################################################################""
def user_logout(request):
    """Log out the currently authenticated user and redirect them to the login page.

    Args:
        request: The HTTP request object.
    Returns:
        A redirect response to the login page.
    """
    auth_logout(request)
    return redirect('login')
############################################################################