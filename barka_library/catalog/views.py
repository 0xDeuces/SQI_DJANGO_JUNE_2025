from django.shortcuts import render, HttpResponse

# Create your views here.
def books(request):
    return HttpResponse("""
        <ul>White House Down</ul>
        <ul>Olympus Has Fallen</ul>
        <ul>Breaking Bad</ul>
        <ul>Merlin</ul>
        <ul>Deuces</ul>
    """)
def featuredBooks(request):
    return HttpResponse("""
        <div>The Famished Road</div>
        <div>Season of Crimson Blossoms</div>
    """)