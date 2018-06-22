from django.db import models

class Album(models.Model):
    artiste = models.CharField(max_length=200)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=150)

    def __str__(self):#returns objects in readble form
        #return self.artiste + ' composed ' + self.album_title
        return self.artiste

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title
