from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import  models

# Create your views here.
def index(request):
	article=models.Article.objects.get(pk=1)
	return render(request,'blog2/index.html',{'article':article})

