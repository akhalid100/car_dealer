from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

# about
def about(request):
    return render(request,'pages/about.html')

# services
def services(request):
    return render(request,'pages/services.html')

# contact
def contact(request):
    return render(request,'pages/contact.html')
