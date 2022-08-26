import re
from unicodedata import name
from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'word_formation/index.html')