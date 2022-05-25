from django.shortcuts import render

from web.models import *

from django.http import JsonResponse
import json

# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")



def home(request):
  playlist_results = Playlist.objects.all()
  return render(request,'web/home.html', {'playlist_results':playlist_results})


def about(request):
  return render(request,'web/about.html')


def author(request, playlist_id):
  return render(request,'web/playlist.html',{'playlist_id':playlist_id})

def data(request):
  query_results = Playlist.objects.all()
  return render(request,"web/data.html",{'query_results':query_results})

def fakejson(request):
  query_results = Playlist.objects.all()
  return render(request,"web/fakejson.html",{'query_results':query_results})

def json(request):
  playlist_results = list(Playlist.objects.values())
  return JsonResponse(playlist_results, safe=False)


