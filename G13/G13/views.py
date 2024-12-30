from django.shortcuts import render

def Main_Home(request):
  return render(request, 'Main.html')