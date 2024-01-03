from django.shortcuts import render, get_object_or_404
from .models import Help

def helps(request):
    helps = Help.objects.all()
    return render(request,'help/helps.html', {'helps':helps})

def help(request, help_id):
    help = get_object_or_404(Help, pk=help_id)
    return render(request,'help/help.html',{'help':help})
