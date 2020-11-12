from django.shortcuts import render
from .models import my_profile
from .models import WhatDoIKnw
# Create your views here.
def home(request):
    profile=my_profile.objects
    Knw=WhatDoIKnw.objects
    return render(request,'home.html',{'profile':profile,'Knw':Knw})
