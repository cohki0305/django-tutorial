from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') # name は何に使う？
]
