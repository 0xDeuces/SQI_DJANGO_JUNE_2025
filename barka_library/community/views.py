from django.shortcuts import render, HttpResponse

# Create your views here.
def events(request):
    return HttpResponse("""
    <section>
    Children’s Book Reading - Saturday 10 AM
    Poetry Night - Friday 6 PM
    </section>
""")