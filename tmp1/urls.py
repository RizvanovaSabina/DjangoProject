from django.urls import path

from tmp.urls import urlpatterns
from tmp1.views import facts,fact1,fact2

urlpatterns = {
    path('facts/',facts),
    path('fact1/',fact1),
    path('fact2/',fact2),
}
