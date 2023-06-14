from django.urls import path

from women.views import *

urlpatterns = [
    path('', index, name="home"),
    path('cats/<slug:cat>/', categories),
    path('archive/<int:year>/', archive),
]