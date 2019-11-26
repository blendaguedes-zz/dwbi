from django.urls import path
from . import views


urlpatterns = [
    # path('import_reserva/', views.reserva_vagas, name='import_tempo'),
    # path('import_deficiencia/', views.deficiencia, name='import_local'),
    # path('import_cursos/', views.curso, name='import_curso'),
    # path('import_ies/', views.localies, name='import_ies'),
    # path('import_bolsa/', views.bolsa_auxilio, name='import_bolsa'),
    # path('import_tempo/', views.tempo, name='import_tempo'),
    #path('fato_aluno_p2/', views.fato_aluno_p2, name='fato_aluno_p2'),
    path('fato_aluno_p3/', views.fato_aluno_p3, name='fato_aluno_p3'),
]