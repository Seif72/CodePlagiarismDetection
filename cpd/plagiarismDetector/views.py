from django.shortcuts import render

def home(request):
    return render(request, 'plagiarismDetector/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'plagiarismDetector/about.html', {'title': 'About'})
