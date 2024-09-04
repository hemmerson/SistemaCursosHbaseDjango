from django.shortcuts import render, redirect
from django.urls import reverse

from sistemacursos.forms import ProfessorForm, AlunoForm, DisciplinaForm, MatriculaForm, ProfDiscForm
from sistemacursos.models import Professor, Aluno, Disciplina


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Views para Professor ==================================================================
def list_professor(request):
    list_obj = Professor.all()
    return render(request, "professor/professor_list.html", {'list_obj': list_obj})

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
    list_obj = Aluno.all()
    return render(request, "aluno/aluno_list.html", {'list_obj': list_obj})

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

# Views para Disciplina =================================================================
def list_disciplina(request):
    list_obj = Aluno.all()
    return render(request, "disciplina/disciplina_list.html", {'list_obj': list_obj})

def create_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(reverse('list_professor'))
    else:
        form = DisciplinaForm()
    return render(request, 'disciplina/disciplina_form.html', {'form': form})

def edit_disciplina(request, numero):
    obj = Disciplina.get(numero)
    if not obj:
        return redirect(reverse('list_diciplina'))

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=obj)
        if form.is_valid():
            updated_obj = form.save(commit=False)
            updated_obj.save()
            return redirect(reverse('list_disciplina'))
    else:
        form = DisciplinaForm(instance=obj)
    return render(request, 'disciplina/disciplina_form.html', {'form': form})

def delete_disciplina(request, numero):
    obj = Disciplina.get(numero)
    if obj:
       if request.method == 'POST':
           obj.delete()
           return redirect(reverse('list_disciplina'))

       else:
           return render(request, 'disciplina/disciplina_delete.html', {'obj': obj})
    return redirect(reverse('list_disciplina'))