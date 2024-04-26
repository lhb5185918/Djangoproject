from django.contrib.auth import authenticate, login
from django.http import HttpResponse



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request.user)
            return HttpResponse("You are logged in")
        else:
            return HttpResponse("Invalid login")

    else:
        return HttpResponse("You are not logged in")
