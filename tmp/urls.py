from django.urls import path

from djngo_project.urls import urlpatterns
from tmp.views import index,kd,chd
from tmp1.views import facts,fact1,fact2
from tmp2.views import ready,set1,go
urlpatterns = [
    path('', index),
    path('kd/', kd),
    path('chd/', chd),


]