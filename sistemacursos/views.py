from django.shortcuts import render, redirect
from django.urls import reverse

from sistemacursos.forms import ProfessorForm, AlunoForm, DisciplinaForm, MatriculaForm, ProfDiscForm
from sistemacursos.models import Professor, Aluno


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Views para Professor ==================================================================
def list_professor(request):
    obj = Professor.all()
    return render(request, "professor/professor_list.html", {'obj': obj})

def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(reverse('list_professor'))
    else:
        form = ProfessorForm()
    return render(request, 'professor/professor_form.html', {'form': form})

def edit_professor(request, numero):
    obj = Professor.get(id)
    if not obj:
        return redirect(reverse('list_professor'))

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=obj)
        if form.is_valid():
            updated_obj = form.save(commit=False)
            updated_obj.save()
            return redirect(reverse('list_professor'))
    else:
        form = ProfessorForm(instance=obj)
    return render(request, 'professor/professor_form.html', {'form': form})

def delete_professor(request, numero):
    obj = Professor.get(id)
    if obj:
       if request.method == 'POST':
           obj.delete()
           return redirect(reverse('list_professor'))

       else:
           return render(request, 'professor/professor_delete.html', {'obj': obj})
    return redirect(reverse('list_professor'))


# Views para Aluno ======================================================================
def list_aluno(request):
    obj = Aluno.all()
    return render(request, "aluno/aluno_list.html", {'obj': obj})

def create_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(reverse('list_aluno'))
    else:
        form = AlunoForm()
    return render(request, 'aluno/aluno_form.html', {'form': form})

def edit_aluno(request, numero):
    obj = Aluno.get(numero)
    if not obj:
        return redirect(reverse('list_aluno'))

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=obj)
        if form.is_valid():
            updated_obj = form.save(commit=False)
            updated_obj.save()
            return redirect(reverse('list_aluno'))
    else:
        form = AlunoForm(instance=obj)
    return render(request, 'aluno/aluno_form.html', {'form': form})

def delete_aluno(request, numero):
    obj = Aluno.get(numero)
    if obj:
       if request.method == 'POST':
           obj.delete()
           return redirect(reverse('list_aluno'))

       else:
           return render(request, 'aluno/aluno_delete.html', {'obj': obj})
    return redirect(reverse('list_aluno'))