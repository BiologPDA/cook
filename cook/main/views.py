from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')

def about(request):
    return render(request, 'main/about.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def reservation(request):
    return render(request, 'main/reservation.html')