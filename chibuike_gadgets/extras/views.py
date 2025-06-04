from django.shortcuts import render, HttpResponse

# Create your views here.
def about(request):
    return HttpResponse('<div> Passionate team delivering innovative solutions with integrity and commitment</div>')