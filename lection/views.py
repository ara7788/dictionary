from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Lection

class LectionDetailView(DetailView):
    model = Lection
    template_name = "lection/lection.html"

def lections(request):
    lections = Lection.objects.order_by('title')
    lections_count = lections.count
    # Only 5 posts on page
    # lections = Lections.objects.order_by('-date')[:6]
    return render(request,'lection/lections.html', {'lections':lections, 'lections_count': lections_count})

def lection(request, lection_id):
    lection = get_object_or_404(Lection, pk=lection_id)
    return render(request,'lection/lection.html',{'lection':lection})
