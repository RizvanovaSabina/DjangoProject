from django.urls import path

from djngo_project.urls import urlpatterns
from tmp.views import index, kd, chd
urlpatterns = {
    path('', index),
    path('kd/', kd),
    path('chd/',chd),
}