from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',                           views.index,   name='index'), # name は何に使う？
    path('<int:question_id>/',         views.detail,  name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/',    views.vote,    name='vote'),
]
