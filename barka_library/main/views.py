from django.shortcuts import render, HttpResponse

# Create your views here.
def welcomeMessage(request):
    return HttpResponse("Message: <h1>Welcome to Barka Street Library</h1>")