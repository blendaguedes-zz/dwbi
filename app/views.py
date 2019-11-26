from django.shortcuts import render
from normalized import models
from warehouse import models as dim
from django.db.models import Count, Sum, Q


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


def fato_aluno_p1(request):
    alunos = models.Aluno.objects.values('alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia').filter(Q(fkcodigosituacao=4) | Q(fkcodigosituacao=5)).annotate(c=Count('idaluno'))
    keys = ['alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia']
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
            print("tentou!")
            codDimLocalIES = dimLocalIES.filter(codOriginalLocalIES=aluno.get('alunocurso__codigocurso__fkcodigoies'))[0]
            codDimCurso = dimCurso.filter(codOriginalCurso=aluno.get('alunocurso__codigocurso'))[0]
            codDimBolsaAuxilio = dimBolsaAuxilio.filter(codOriginalBolsaAuxilio=aluno.get('fkcodigoapoiosocial'))[0]
            codDimDeficiencia = dimDeficiencia.filter(codOriginalDeficiencia=aluno.get('fkdeficiencia'))[0]
            codDimReservaVagas = dimReservaVagas.filter(codOriginalReservaVagas=aluno.get('fkreservavagas'))[0]

            print(codDimBolsaAuxilio, codDimTempo, codDimDeficiencia, codDimReservaVagas, codDimLocalIES)
            if(codDimLocalIES and codDimCurso and codDimBolsaAuxilio and codDimDeficiencia and codDimReservaVagas):

                fato_aluno = dim.FatoAluno.objects.create(codCursoPk=codDimCurso,
                                                          codLocalIESPk=codDimLocalIES,
                                                          codTempoPk=codDimTempo,
                                                          codReservaVagasPk=codDimReservaVagas,
                                                          codDeficienciaPk=codDimDeficiencia,
                                                          codBolsaAuxilioPk=codDimBolsaAuxilio,
                                                          indiceDesistenciaDeficiencia=aluno.get('c'))

                fato_aluno.save()
            else:
                continue
        except:
            print("fail")
            continue

    return render(request, 'app/aluna.html',)

def fato_aluno_p1(request):
    alunos = models.Aluno.objects.values('alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia').filter(Q(fkcodigosituacao=4) | Q(fkcodigosituacao=5)).annotate(c=Count('idaluno'))
    keys = ['alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia']
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
            print("tentou!")
            codDimCurso = dimCurso.filter(codOriginalCurso=aluno.get(keys[0]))[0]
            codDimLocalIES = dimLocalIES.filter(codOriginalLocalIES=aluno.get(keys[1]))[0]
            codDimBolsaAuxilio = dimBolsaAuxilio.filter(codOriginalBolsaAuxilio=aluno.get(keys[2]))[0]
            codDimReservaVagas = dimReservaVagas.filter(codOriginalReservaVagas=aluno.get(keys[3]))[0]
            codDimDeficiencia = dimDeficiencia.filter(codOriginalDeficiencia=aluno.get(keys[4]))[0]

            print(codDimBolsaAuxilio, codDimTempo, codDimDeficiencia, codDimReservaVagas, codDimLocalIES)
            if(codDimLocalIES and codDimCurso and codDimBolsaAuxilio and codDimDeficiencia and codDimReservaVagas):

                fato_aluno = dim.FatoAluno.objects.create(codCursoPk=codDimCurso,
                                                          codLocalIESPk=codDimLocalIES,
                                                          codTempoPk=codDimTempo,
                                                          codReservaVagasPk=codDimReservaVagas,
                                                          codDeficienciaPk=codDimDeficiencia,
                                                          codBolsaAuxilioPk=codDimBolsaAuxilio,
                                                          indiceDesistenciaDeficiencia=aluno.get('c'))

                fato_aluno.save()
            else:
                continue
        except:
            print("fail")
            continue

    return render(request, 'app/aluna.html',)

def fato_aluno_p2(request):
    alunos = models.Aluno.objects.values('alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia').filter(Q(inconcluente=1) & Q(alunocurso__codigocurso__fkcodigoies__fkcodigocategoriaadministrativa=2)).annotate(c=Count('idaluno'))
    keys = ['alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia']
    codDimTempo = dim.DimTempo.objects.filter(codOriginalTempo=1)[0]
    dimCurso = dim.DimCurso.objects
    dimBolsaAuxilio = dim.DimBolsaAuxilio.objects
    dimReservaVagas = dim.DimReservaVagas.objects
    dimLocalIES = dim.DimLocalIES.objects
    dimDeficiencia = dim.DimDeficiencia.objects


    count = 1
    for aluno in alunos:
        if None in aluno.values():
            continue
        try:
            codDimCurso = dimCurso.filter(codOriginalCurso=aluno.get(keys[0]))[0]
            codDimLocalIES = dimLocalIES.filter(codOriginalLocalIES=aluno.get(keys[1]))[0]
            codDimBolsaAuxilio = dimBolsaAuxilio.filter(codOriginalBolsaAuxilio=aluno.get(keys[2]))[0]
            codDimReservaVagas = dimReservaVagas.filter(codOriginalReservaVagas=aluno.get(keys[3]))[0]
            codDimDeficiencia = dimDeficiencia.filter(codOriginalDeficiencia=aluno.get(keys[4]))[0]

            if(codDimLocalIES and codDimCurso and codDimBolsaAuxilio and codDimDeficiencia and codDimReservaVagas):

                fato_aluno = dim.FatoAluno.objects.filter(codCursoPk=codDimCurso,
                                                          codLocalIESPk=codDimLocalIES,
                                                          codTempoPk=codDimTempo,
                                                          codReservaVagasPk=codDimReservaVagas,
                                                          codDeficienciaPk=codDimDeficiencia,
                                                          codBolsaAuxilioPk=codDimBolsaAuxilio).first()
                if(fato_aluno):
                    fato_aluno.indiceIngressantesConcluintesRegiaoEstadual = aluno.get('c')
                    fato_aluno.save()
                    #print("update")

                else:

                    fato_aluno = dim.FatoAluno.objects.create(codCursoPk=codDimCurso,
                                                              codLocalIESPk=codDimLocalIES,
                                                              codTempoPk=codDimTempo,
                                                              codReservaVagasPk=codDimReservaVagas,
                                                              codDeficienciaPk=codDimDeficiencia,
                                                              codBolsaAuxilioPk=codDimBolsaAuxilio,
                                                              indiceIngressantesConcluintesRegiaoEstadual=aluno.get('c'))
                    fato_aluno.save()
                    #print("create")
            else:

                continue
        except:
            print("fail")


    return render(request, 'app/aluna.html',)


def fato_aluno_p3(request):
    alunos = models.Aluno.objects.values('alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia').filter(Q(fkcodigosituacao=4) & ~Q(fkreservavagas=1)).annotate(c=Count('idaluno'))
    keys = ['alunocurso__codigocurso','alunocurso__codigocurso__fkcodigoies','fkcodigoapoiosocial', 'fkreservavagas','fkdeficiencia']
    codDimTempo = dim.DimTempo.objects.filter(codOriginalTempo=1)[0]
    dimCurso = dim.DimCurso.objects
    dimBolsaAuxilio = dim.DimBolsaAuxilio.objects
    dimReservaVagas = dim.DimReservaVagas.objects
    dimLocalIES = dim.DimLocalIES.objects
    dimDeficiencia = dim.DimDeficiencia.objects


    count = 1
    for aluno in alunos:
        if None in aluno.values():
            continue
        try:
            codDimCurso = dimCurso.filter(codOriginalCurso=aluno.get(keys[0]))[0]
            codDimLocalIES = dimLocalIES.filter(codOriginalLocalIES=aluno.get(keys[1]))[0]
            codDimBolsaAuxilio = dimBolsaAuxilio.filter(codOriginalBolsaAuxilio=aluno.get(keys[2]))[0]
            codDimReservaVagas = dimReservaVagas.filter(codOriginalReservaVagas=aluno.get(keys[3]))[0]
            codDimDeficiencia = dimDeficiencia.filter(codOriginalDeficiencia=aluno.get(keys[4]))[0]

            if(codDimLocalIES and codDimCurso and codDimBolsaAuxilio and codDimDeficiencia and codDimReservaVagas):

                fato_aluno = dim.FatoAluno.objects.filter(codCursoPk=codDimCurso,
                                                          codLocalIESPk=codDimLocalIES,
                                                          codTempoPk=codDimTempo,
                                                          codReservaVagasPk=codDimReservaVagas,
                                                          codDeficienciaPk=codDimDeficiencia,
                                                          codBolsaAuxilioPk=codDimBolsaAuxilio).first()
                if(fato_aluno):
                    fato_aluno.indiceDesistenciaReservaVagasRegiao = aluno.get('c')
                    fato_aluno.save()
                    #print("update")

                else:

                    fato_aluno = dim.FatoAluno.objects.create(codCursoPk=codDimCurso,
                                                              codLocalIESPk=codDimLocalIES,
                                                              codTempoPk=codDimTempo,
                                                              codReservaVagasPk=codDimReservaVagas,
                                                              codDeficienciaPk=codDimDeficiencia,
                                                              codBolsaAuxilioPk=codDimBolsaAuxilio,
                                                              indiceDesistenciaReservaVagasRegiao=aluno.get('c'))
                    fato_aluno.save()
                    #print("create")
            else:

                continue
        except:
            print("fail")


    return render(request, 'app/index.html',)

