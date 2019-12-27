from django.shortcuts import render




def home(request):
    return render(request,'welcomeapp/home.html')
def company(request):
    return render(request,'welcomeapp/company.html')
def programs(request):
    return render(request,'welcomeapp/programs.html')
