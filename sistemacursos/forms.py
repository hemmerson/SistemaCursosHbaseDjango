from django import forms
from models import *

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        widgets = {
            'numero_prof': forms.TextInput(attrs={'class': 'form-control'}),
            'profnome': forms.TextInput(attrs={'class': 'form-control'}),
            'profrua': forms.TextInput(attrs={'class': 'form-control'}),
            'profcidade': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'numero_aluno': forms.TextInput(attrs={'class': 'form-control'}),
            'alunome': forms.TextInput(attrs={'class': 'form-control'}),
            'alufrua': forms.TextInput(attrs={'class': 'form-control'}),
            'alucidade': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
        widgets = {
            'codigo_disc': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_disciplina': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_curso': forms.TextInput(attrs={'class': 'form-control'}),
            'qtd': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MatriculaForm(forms.ModelForm):
    numero_aluno = forms.ModelChoiceField(
        queryset=Aluno.all(),
        label="Aluno",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    codigo_disc = forms.ModelChoiceField(
        queryset=Disciplina.all(),
        label="Disciplina",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'ano': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfDiscForm(forms.ModelForm):
    numero_prof = forms.ModelChoiceField(
        queryset=Professor.all(),
        label="Professor",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    codigo_disc = forms.ModelChoiceField(
        queryset=Disciplina.all(),
        label="Disciplina",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = ProfDisc
        fields = '__all__'
        widgets = {
            'ano': forms.TextInput(attrs={'class': 'form-control'}),
        }
