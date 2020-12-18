from django.shortcuts import render
from login.loginController import login_con
from login.loginForm import LoginForm


def index(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Saved&Valid")
            form.save()
            return login_con(request)
    else:
        print("For GET request")
        form = LoginForm()
    return render(request, 'loginForm.html', {'form': form})
