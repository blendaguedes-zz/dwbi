from django.shortcuts import render
from warehouse import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



def tempo(request):
    tempo_list = models.DimTempo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tempo_list, 50)
    try:
        tempos = paginator.page(page)
    except PageNotAnInteger:
        tempos = paginator.page(1)
    except EmptyPage:
        tempos = paginator.page(paginator.num_pages)
    return render(request, 'app/tempo.html', {'tempo': tempos})


def local(request):
    locals_list = models.DimLocalIES.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(locals_list, 50)
    try:
        locals = paginator.page(page)
    except PageNotAnInteger:
        locals = paginator.page(1)
    except EmptyPage:
        locals = paginator.page(paginator.num_pages)
    return render(request, 'app/local.html', {'locals': locals})


def curso(request):
    cursos_list = models.DimCurso.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(cursos_list, 50)
    try:
        cursos = paginator.page(page)
    except PageNotAnInteger:
        cursos = paginator.page(1)
    except EmptyPage:
        cursos = paginator.page(paginator.num_pages)

    return render(request, 'app/cursos.html', {'cursos': cursos})


def aluna(request):
    aluna_list = models.FatoAluno.objects.all().filter(~Q(indiceDesistenciaReservaVagasRegiao=None))
    page = request.GET.get('page', 1)

    paginator = Paginator(aluna_list, 50)
    try:
        alunas = paginator.page(page)
    except PageNotAnInteger:
        alunas = paginator.page(1)
    except EmptyPage:
        alunas = paginator.page(paginator.num_pages)

    return render(request, 'app/aluna.html', {'alunas': alunas})