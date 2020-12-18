from django.shortcuts import render
from login.loginAPIService import login_con
from login.loginForm import LoginForm


def index(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            form.save()
            return login_con(request)
    else:

        form = LoginForm()
    return render(request, 'loginForm.html', {'form': form})
