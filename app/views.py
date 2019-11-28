from django.shortcuts import render
from normalized import models
from warehouse import models as dim
from django.db.models import Count, Q, QuerySet


def curso(request):
    cursos_norm = models.Curso.objects.all()
    for l in cursos_norm:
        dim_local = dim.DimCurso.objects.create(codOriginalCurso=l.codigocurso,
                                                nomeCurso=l.nomecurso,
                                                quantidadeIngresso=l.quantidadeingressocurso,
                                                quantidadeConcluinte=l.quantidadeconcluintecurso,
                                                grauAcademico=l.fkcodigograuacademico.idgrauacademico,
                                                turno=l.fkcodigoturno.codigoturno,
                                                capital=l.incapitalcurso)
        dim_local.save()
    return render(request, 'app/index.html')


def tempo(request):
    tempo_norm = models.Tempo.objects.all()

    for tempo in tempo_norm:

        dim_tempo = dim.DimTempo.objects.create(codOriginalTempo=tempo.codigotempo,
                                                ano=tempo.ano)
        print(dim_tempo.ano, dim_tempo.codOriginalTempo)
        dim_tempo.save()
    return render(request, 'app/index.html')


def bolsa_auxilio(request):
    bolsa_norm = models.Apoiosocial.objects.all()

    for bolsa in bolsa_norm:
        dim_bolsa = dim.DimBolsaAuxilio.objects.create(codOriginalBolsaAuxilio=bolsa.idapoiosocial)
        dim_bolsa.save()
    return render(request, 'app/index.html')

def reserva_vagas(request):
    bolsa_norm = models.Reservavagas.objects.all()

    for bolsa in bolsa_norm:
        dim_bolsa = dim.DimReservaVagas.objects.create(codOriginalReservaVagas=bolsa.idreservavagas)
        dim_bolsa.save()
    return render(request, 'app/index.html')

def deficiencia(request):
    bolsa_norm = models.Deficiencia.objects.all()

    for bolsa in bolsa_norm:
        dim_bolsa = dim.DimDeficiencia.objects.create(codOriginalDeficiencia=bolsa.iddeficiencia)
        dim_bolsa.save()
    return render(request, 'app/index.html')

def get_nome_uf(codigo):
    curso = models.Curso.objects.filter(fkcodigoies=codigo).first()

    if curso:
        uf = curso.fkcodigolocaloferta.siglauf
    else:
        uf = None
    return uf


def get_nome_regiao(codigo):
    regiao = models.Curso.objects.filter(fkcodigoies=codigo).only('fkcodigolocaloferta').first().fkcodigolocaloferta.nomeregiao

    return regiao


def localies(request):
    ies_norm = models.Ies.objects.all()
    #ies_codigos_original = dim.DimLocalIES.objects.values_list('codOriginalLocalIES', flat=True)
    for ies in ies_norm:
        nome_uf = get_nome_uf(ies.idcodigoies)
        if nome_uf: #and ies.idcodigoies not in ies_codigos_original:
            nome_regiao = get_nome_regiao(ies.idcodigoies)
            dim_ies = dim.DimLocalIES.objects.create(codOriginalLocalIES=ies.idcodigoies,
                                                     nomeRegiao=nome_regiao,
                                                     categoriaAdmistrativa=ies.fkcodigocategoriaadministrativa.idcategoriaadministrativa,
                                                     nomeUF=nome_uf)
            dim_ies.save()

    return render(request, 'app/index.html')


def fato_aluno_maker(request, filtro, campo_indice):
    alunos = models.Aluno.objects.values('alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies',
                                         'fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia').filter(filtro).annotate(c=Count('idaluno'))
    keys = ['alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial',
            'fkreservavagas','fkdeficiencia']

    codDimTempo = dim.DimTempo.objects.filter(codOriginalTempo=1)[0]
    dimCurso = dim.DimCurso.objects
    dimBolsaAuxilio = dim.DimBolsaAuxilio.objects
    dimReservaVagas = dim.DimReservaVagas.objects
    dimLocalIES = dim.DimLocalIES.objects
    dimDeficiencia = dim.DimDeficiencia.objects

    for aluno in alunos:
        if None in aluno.values():
            continue
        try:
            codDimCurso = dimCurso.filter(codOriginalCurso=aluno.get(keys[0]))[0]
            codDimLocalIES = dimLocalIES.filter(codOriginalLocalIES=aluno.get(keys[1]))[0]
            codDimBolsaAuxilio = dimBolsaAuxilio.filter(codOriginalBolsaAuxilio=aluno.get(keys[2]))[0]
            codDimReservaVagas = dimReservaVagas.filter(codOriginalReservaVagas=aluno.get(keys[3]))[0]
            codDimDeficiencia = dimDeficiencia.filter(codOriginalDeficiencia=aluno.get(keys[4]))[0]
            indice = aluno.get('c')

            if codDimLocalIES and codDimCurso and codDimBolsaAuxilio and codDimDeficiencia and codDimReservaVagas :

                fato_aluno = dim.FatoAluno.objects.filter(codCursoPk=codDimCurso,
                                                          codLocalIESPk=codDimLocalIES,
                                                          codTempoPk=codDimTempo,
                                                          codReservaVagasPk=codDimReservaVagas,
                                                          codDeficienciaPk=codDimDeficiencia,
                                                          codBolsaAuxilioPk=codDimBolsaAuxilio).first()
                if fato_aluno:
                    fato_aluno.campo_indice = indice
                    fato_aluno.save()
                else:
                    fato_aluno = dim.FatoAluno.objects.create(codCursoPk=codDimCurso,
                                                              codLocalIESPk=codDimLocalIES,
                                                              codTempoPk=codDimTempo,
                                                              codReservaVagasPk=codDimReservaVagas,
                                                              codDeficienciaPk=codDimDeficiencia,
                                                              codBolsaAuxilioPk=codDimBolsaAuxilio)
                    setattr(fato_aluno, campo_indice, indice)
                    fato_aluno.save()
            else:
                continue

        except Exception as e:
            print(e)
            print("fail")

    return render(request, 'app/index.html',)


def fato_aluno_p1(request):
    filtro = Q(fkcodigosituacao=4) | Q(fkcodigosituacao=5)
    campo_indice = "indiceDesistenciaDeficiencia"

    fato_aluno_maker(request, filtro, campo_indice)


def fato_aluno_p2_federal_ingressante(request):
    filtro = (Q(iningressototal=1) | Q(iningressovaganova=1)) & Q(alunocurso__codigocurso__fkcodigoies__fkcodigocategoriaadministrativa=1)
    campo_indice = "indiceIngressantesRegiaoFederal"

    return fato_aluno_maker(request, filtro, campo_indice)


def fato_aluno_p2_federal_concluinte(request):
    filtro = (Q(inconcluente=1)) & Q(alunocurso__codigocurso__fkcodigoies__fkcodigocategoriaadministrativa=1)
    campo_indice = "indiceConcluintesRegiaoFederal"

    return fato_aluno_maker(request, filtro, campo_indice)


def fato_aluno_p2_estadual_ingressante(request):
    filtro = (Q(iningressototal=1) | Q(iningressovaganova=1)) & Q(alunocurso__codigocurso__fkcodigoies__fkcodigocategoriaadministrativa=2)
    campo_indice = "indiceIngressantesRegiaoEstadual"

    fato_aluno_maker(request, filtro, campo_indice)


def fato_aluno_p2_estadual_concluinte(request):
    filtro = (Q(inconcluente=1)) & Q(alunocurso__codigocurso__fkcodigoies__fkcodigocategoriaadministrativa=2)
    campo_indice = "indiceConcluintesRegiaoEstadual"

    fato_aluno_maker(request, filtro, campo_indice)


def fato_aluno_p3(request):
    campo_indice = "indiceDesistenciaReservaVagasRegiao"
    filtro = (Q(fkcodigosituacao=4) | Q(fkcodigosituacao=5)) & ~Q(fkreservavagas=1)
    fato_aluno_maker(request, campo_indice, filtro)

