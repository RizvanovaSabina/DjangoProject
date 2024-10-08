from django.urls import path
from tmp.urls import urlpatterns
from tmp2.views import ready,set1,go

urlpatterns = {
    path('ready/',ready),
    path('set1/',set1),
    path('go/',go),
}