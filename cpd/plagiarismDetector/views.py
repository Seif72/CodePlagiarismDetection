from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import PythonFile
from .forms import PythonFileForm

def home(request):
    return render(request, 'plagiarismDetector/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'plagiarismDetector/about.html', {'title': 'About'})

def upload(request):
    if request.method == 'POST':
        form = PythonFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        form =  PythonFileForm()
    return render(request, 'plagiarismDetector/upload.html', {'title': 'Upload', 'form': form})