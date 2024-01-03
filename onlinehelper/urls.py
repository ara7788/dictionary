from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from .views import OnlineHelperDetailView

app_name = 'onlinehelper'

urlpatterns = [
    path('', views.onlinehelpers, name='onlinehelpers'),
    path('<int:onlinehelper_id>/', views.onlinehelper, name='onlinehelper'),
    path("<slug:slug>", views.OnlineHelperDetailView.as_view(), name="onlinehelper_detail"),
    path('<slug:slug>/',views.show_onlinehelper, name='onlinehelper_slug'),

    # path('spark/', views.spark, name='spark'),
    # path('kafka/', views.kafka, name='kafka'),
    # path('flink/', views.flink, name='flink'),
    # path('hadoop/', views.hadoop, name='hadoop'),
    # path('storm/', views.storm, name='storm'),
    # path('samza/', views.samza, name='samza'),
    # path('analysis/', views.analysis, name='analysis'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)