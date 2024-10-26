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

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def dishes(request):
    return render(request, 'main/dishes.html')

def main_dish(request):
    return render(request, 'main/main_dish.html')

def desserts(request):
    return render(request, 'main/desserts.html')

def bar(request):
    return render(request, 'main/bar.html')