from django.shortcuts import render

from sistemacursos.models import Professor


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Views para Professor ==================================================================
def list_professor(request):
    professors = Professor.all()
    return render(request, "professor/professor_list.html", {'professors': professors})