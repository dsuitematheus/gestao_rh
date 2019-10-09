from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required #da obrigatoriedade do usuario estar logado para acessar
def home(request):
    return render(request, 'core/index.html')
