from django.shortcuts import render, get_object_or_404
from .models import Home

def homes(request):
    homes = Home.objects.all()
    return render(request,'home/homes.html', {'homes':homes})

def home(request, home_id):
    home = get_object_or_404(Home, pk=home_id)
    return render(request,'home/home.html',{'home':home})

