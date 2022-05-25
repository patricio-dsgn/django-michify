from django.db import models
from django.utils import timezone

from django.db.models import Model

class Playlist(models.Model):   
  url = models.CharField(max_length=100,default='')
  author = models.CharField(max_length=100,default='')
  text = models.TextField()
  tags_author = models.CharField(max_length=300,default='')
  tags_playlist = models.CharField(max_length=300,default='')
  link = models.CharField(max_length=300,default='')
  image = models.ImageField(upload_to='media/covers/',default='')

class Post(models.Model):
  idm = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  text = models.TextField()
  photo = models.ImageField(
    upload_to='media/photo_posts',
    default='media/default/default.jpg',
    blank=True)


class Suscriptor(models.Model):
  full_name = models.CharField(max_length=100)
  email = models.CharField(max_length=1000)





# -----------------------------------------
class Contact(models.Model): 
  name = models.CharField(max_length=200)
  sender = models.EmailField()
  subject = models.CharField(max_length=200)
  message = models.TextField()
  cc_myself = models.BooleanField(default=False)
  sending_date = models.DateTimeField(blank=True, null=True)

  def sent(self):
    self.sending_date = timezone.now()
    self.save()

  def str(self):
    return self.sender

