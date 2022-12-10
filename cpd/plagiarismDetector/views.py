from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'plagiarismDetector/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'plagiarismDetector/about.html', {'title': 'About'})

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'plagiarismDetector/upload.html', {'file_url': file_url})
    return render(request, 'plagiarismDetector/upload.html')