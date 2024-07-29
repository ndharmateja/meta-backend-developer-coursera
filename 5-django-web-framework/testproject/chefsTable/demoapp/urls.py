from django.urls import path, re_path
from demoapp import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('hello', views.hello, name='hello'),
    re_path(r'^menu/([0-9]{2})/$', views.re_view, name="re_view")
] 