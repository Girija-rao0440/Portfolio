from django.shortcuts import render
from .models import blog
# Create your views here.
def blogs(request):
    blog=blog.objects
    return render(request,'blogs.html',{'blog':blog})
