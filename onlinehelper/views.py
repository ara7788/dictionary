from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import OnlineHelper

class OnlineHelperDetailView(DetailView):
    model = OnlineHelper
    template_name = "onlinehelper/onlinehelper.html"

def onlinehelpers(request):
    onlinehelpers = OnlineHelper.objects.order_by('title')
    onlinehelpers_count = onlinehelpers.count()
    # Only 5 posts on page
    # onlinehelpers = OnlineHelper.objects.order_by('-date')[:5]
    return render(request,'onlinehelper/onlinehelpers.html', {'onlinehelpers':onlinehelpers, 'onlinehelpers_count': onlinehelpers_count})

def onlinehelper(request, onlinehelper_id=1):
    onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
    return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper})

def show_onlinehelper(request, slug):
    onlinehelper = get_object_or_404(OnlineHelper, slug=slug)
    return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper})

# def spark(request, char_name='Spark', msg=None):
#     if char_name != None:
#         # onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
#         onlinehelper = OnlineHelper.objects.get(title__icontains=char_name)
#         if onlinehelper:
#             print(onlinehelper)
#         else:
#             msg = 'No item were found in the query.'
#             print(msg)
#     return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper, 'msg': msg})

# def kafka(request, char_name='Kafka', msg=None):
#     if char_name != None:
#         # onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
#         onlinehelper = OnlineHelper.objects.get(title__icontains=char_name)
#         if onlinehelper:
#             print(onlinehelper)
#         else:
#             msg = 'No item were found in the query.'
#             print(msg)
#     return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper, 'msg': msg})

# def flink(request, char_name='Flink', msg=None):
#     if char_name != None:
#         # onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
#         onlinehelper = OnlineHelper.objects.get(title__icontains=char_name)
#         if onlinehelper:
#             print(onlinehelper)
#         else:
#             msg = 'No item were found in the query.'
#             print(msg)
#     return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper, 'msg': msg})

# def hadoop(request, char_name='Hadoop', msg=None):
#     if char_name != None:
#         # onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
#         onlinehelper = OnlineHelper.objects.get(title__icontains=char_name)
#         if onlinehelper:
#             print(onlinehelper)
#         else:
#             msg = 'No item were found in the query.'
#             print(msg)
#     return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper, 'msg': msg})

# def storm(request, char_name='Storm', msg=None):
#     if char_name != None:
#         # onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
#         onlinehelper = OnlineHelper.objects.get(title__icontains=char_name)
#         if onlinehelper:
#             print(onlinehelper)
#         else:
#             msg = 'No item were found in the query.'
#             print(msg)
#     return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper, 'msg': msg})

# def samza(request, char_name='Samza', msg=None):
#     if char_name != None:
#         # onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
#         onlinehelper = OnlineHelper.objects.get(title__icontains=char_name)
#         if onlinehelper:
#             print(onlinehelper)
#         else:
#             msg = 'No item were found in the query.'
#             print(msg)
#     return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper, 'msg': msg})

# def analysis(request, char_name='Analysis', msg=None):
#     if char_name != None:
#         # onlinehelper = get_object_or_404(OnlineHelper, pk=onlinehelper_id)
#         onlinehelper = OnlineHelper.objects.get(title__icontains=char_name)
#         if onlinehelper:
#             print(onlinehelper)
#         else:
#             msg = 'No item were found in the query.'
#             print(msg)
#     return render(request,'onlinehelper/onlinehelper.html', {'onlinehelper':onlinehelper, 'msg': msg})
