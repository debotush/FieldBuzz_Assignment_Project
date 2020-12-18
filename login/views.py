from django.shortcuts import render

from login.loginForm import LoginForm


def index(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Saved&Valid")
            form.save()
    else:
        print("NotSaved&Valid")
        form = LoginForm()
    return render(request, 'loginForm.html', {'form': form})
