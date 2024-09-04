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

    path('disciplinas/lista/', list_disciplina, name='list_disciplina'),
    path('disciplinas/novo/', create_disciplina, name='create_disciplina'),
    path('disciplinas/update/<str:numero>', edit_disciplina, name='edit_disciplina'),
    path('disciplinas/delete/<str:numero>', delete_disciplina, name='delete_disciplina'),

]