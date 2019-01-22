from django.conf import settings
from django.shortcuts import render, redirect, render_to_response
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Document
from .tesseract_ocr import searchable_pdf
import os

def index(request):
    return render(request, 'app_main/login.html')

def test(request):
    return render(request, 'app_main/test.html')

def test2(request):
    return render(request, 'app_main/test2.html')

def viewerjs(request):
    return render(request, 'app_main/web/viewer.html?file=')

def dash(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = Document.objects.all()
            return render_to_response('app_main/uploaded-files.html', { 'data' : data })
    else:
        form = DocumentForm()
    return render(request, 'app_main/dash.html', {
        'form' : form
    })
        
    
def uploadedfiles(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = Document.objects.all()
            form = DocumentForm()
            return render_to_response('app_main/uploaded-files.html', { 'data' : data })
    else:
        data = Document.objects.all()
        form = DocumentForm()
    return render(request, 'app_main/uploaded-files.html', {
        'form' : form,
        'data' : data,
    })

def docviews(request):
    return render(request, 'app_main/doc_view.html')




