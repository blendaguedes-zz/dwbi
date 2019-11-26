from django.urls import path
from . import views


urlpatterns = [
    path('dimtempo/', views.tempo, name='tempo'),
    path('dimlocal/', views.local, name='local'),
    path('dimcurso/', views.curso, name='curso'),
    path('fatoaluna/', views.aluna, name='aluna')
]