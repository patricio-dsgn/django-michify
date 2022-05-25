from django.shortcuts import render,redirect

from web.models import *

from django.http import JsonResponse
import json

# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# -------------------------------------------------------
# from django import forms
from django.core.mail import send_mail#, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.utils import timezone
from .models import *
from .forms import *


def admin(request):
  return redirect('admin/')


def home(request):
  playlist_results = Playlist.objects.all()
  return render(request,'web/home.html', {'playlist_results':playlist_results})





def all(request):
  playlist_results = Playlist.objects.all()
  return render(request,'web/all.html', {'playlist_results':playlist_results, 'sel':'all'})


def about(request):
  return render(request,'web/about.html',{'sel':'about'})

def contact(request):
  return render(request,'web/contact.html',{'sel':'contact'})

def subscribe(request):
  return render(request,'web/subscribe.html',{'sel':'subscribe'})

def blog(request):
  return render(request,'web/blog.html',{'sel':'blog'})


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






# ---------------------------------------------

def contact(request):
  if request.method == 'GET':
    form = ContactForm()
  else:
    form = ContactForm(request.POST)
    if form.is_valid():
      contact = form.save()
      name = form.cleaned_data['name']
      sender = form.cleaned_data['sender']
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']
      cc_myself = form.cleaned_data['cc_myself']
      contact.sending_date = timezone.now()
      contact.save()

      recipients = []
      if cc_myself:
        recipients.append(sender)

      send_mail(subject, message,"", recipients)
      # The signature for the send_email method is:
      # send_mail(subject, message, from_email, recipient_list, fail_silently=False, 
      # auth_user=None, auth_password=None, connection=None, html_message=None)
      return redirect('success')
  return render(request, "web/contact.html", {'sel':'contact','form': form})

def success(request):
  return render(request, 'web/success.html', {'success': success})


def message_list(request):
  messages = Contact.objects.order_by('sending_date')
  return render(request, 'web/message_list.html', {'messages': messages})


@login_required
def my_messages(request):
  email = request.user.email
  my_messages = Contact.objects.filter(sender=email).all().order_by('sending_date')
  return render(request, 'web/my_messages.html', {'my_messages': my_messages})


def message_detail(request,pk):
  message = get_object_or_404(Contact, pk=pk)
  return render(request, 'web/message_detail.html', {'message': message})


@login_required
def message_remove(request,pk):
  message = get_object_or_404(Contact, pk=pk)
  message.delete()
  return redirect('message_list')


