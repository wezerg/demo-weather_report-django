from django.urls import path

from . import views

app_name = 'timer'
urlpatterns = [
    path('', views.index, name='index'),
    path('test1', views.test1, name="test1")
]