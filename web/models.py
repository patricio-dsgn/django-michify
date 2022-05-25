from django.db import models

class Playlist(models.Model):   
  url = models.CharField(max_length=100,default='')
  author = models.CharField(max_length=100,default='')
  text = models.CharField(max_length=300,default='')
  tags_author = models.CharField(max_length=100,default='')
  tags_playlist = models.CharField(max_length=100,default='')
  link = models.CharField(max_length=300,default='')
  image = models.ImageField(upload_to='media/covers/',default='')
