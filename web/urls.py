from django.conf.urls import handler404

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('data', views.data, name='data'),
    path('fakejson', views.fakejson, name='fakejson'),
    path('json', views.json, name='json'),

    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<str:playlist_id>/', views.author, name='author'),
    # ex: /polls/5/results/

    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

