from xml.etree.ElementInclude import include
from django.urls import path,include
from . import views
import debug_toolbar

urlpatterns = [
    path('login/',views.start),
    path('register/',views.register),
    path('task/',views.task),
    path('welcome/',views.welcome),
    path('__debug__/',include(debug_toolbar.urls))
]
