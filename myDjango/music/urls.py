from django.conf.urls import url
from . import views

urlpatterns = [
    #/music/
    url(r'^$',views.index,name='index'),
    #music/album_id e.g 120/
    url(r'^(?P<album_id>[0-9]+)/',views.display,name='display'),

]
