from django.shortcuts import render, HttpResponse

# Create your views here.
def gadgets(request):
    return HttpResponse('<ul> <li>iphone</li>'
    '<li>samsung</li>'
    '<li>headphones</li>'
    '<li>TV</li> </ul>')