from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Framework

class FrameworkDetailView(DetailView):
    model = Framework
    template_name = "framework/framework.html"

def frameworks(request):
    frameworks = Framework.objects.order_by('title')
    frameworks_count = frameworks.count
    # Only 5 posts on page
    # frameworks = Frameworks.objects.order_by('-date')[:5]
    return render(request,'framework/frameworks.html', {'frameworks':frameworks, 'frameworks_count': frameworks_count})

def framework(request, framework_id):
    framework = get_object_or_404(Framework, pk=framework_id)
    return render(request,'framework/framework.html',{'framework':framework})
