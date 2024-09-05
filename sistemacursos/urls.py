from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('professores/lista/', list_professor, name='list_professor'),
    path('professores/novo/', create_professor, name='create_professor'),
    path('professores/update/<str:numero>', edit_professor, name='edit_professor'),
    path('professores/delete/<str:numero>', delete_professor, name='delete_professor'),

    path('alunos/lista/', list_aluno, name='list_aluno'),
    path('alunos/novo/', create_aluno, name='create_aluno'),
    path('alunos/update/<str:numero>', edit_aluno, name='edit_aluno'),
    path('alunos/delete/<str:numero>', delete_aluno, name='delete_aluno'),

    path('matriculas/lista/', list_matricula, name='list_matricula'),
    path('matriculas/nova/', create_matricula, name='create_matricula'),
    path('matriculas/editar/<str:numero_aluno>/<str:codigo_disc>/<str:ano>/', edit_matricula, name='edit_matricula'),
    path('matriculas/excluir/<str:numero_aluno>/<str:codigo_disc>/<str:ano>/', delete_matricula,
         name='delete_matricula'),

    path('profdiscs/lista/', list_profdisc, name='list_profdisc'),
    path('profdiscs/nova/', create_profdisc, name='create_profdisc'),
    path('profdiscs/editar/<str:numero_prof>/<str:codigo_disc>/<str:ano>/', edit_profdisc, name='edit_profdisc'),
    path('profdiscs/excluir/<str:numero_prof>/<str:codigo_disc>/<str:ano>/', delete_profdisc,
         name='delete_profdisc'),



]