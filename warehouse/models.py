from django.db import models


class DimTempo(models.Model):
    codTempo = models.AutoField(primary_key=True)
    codOriginalTempo = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)


class DimLocalIES(models.Model):
    codLocalIES = models.AutoField(primary_key=True)
    codOriginalLocalIES = models.IntegerField(blank=True, null=True)
    nomeRegiao = models.CharField(blank=True, null=True, max_length=40)
    categoriaAdmistrativa = models.IntegerField(blank=True, null=True)
    nomeUF = models.CharField(blank=True, null=True, max_length=2)


class DimCurso(models.Model):
    codCurso = models.AutoField(primary_key=True)
    codOriginalCurso = models.IntegerField(blank=False, null=False, )
    nomeCurso = models.CharField(blank=False, null=False, max_length=255)
    quantidadeIngresso = models.IntegerField(blank=True, null=True)
    quantidadeConcluinte = models.IntegerField(blank=True, null=True)
    grauAcademico = models.IntegerField(blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    capital = models.BooleanField(blank=False, default=False)


class DimBolsaAuxilio(models.Model):
    codBolsaAuxilio = models.AutoField(primary_key=True)
    codOriginalBolsaAuxilio = models.IntegerField(blank=True, null=True)


class DimReservaVagas(models.Model):
    codReservaVagas = models.AutoField(primary_key=True)
    codOriginalReservaVagas = models.IntegerField(blank=True, null=True)


class DimDeficiencia(models.Model):
    codDeficiencia = models.AutoField(primary_key=True)
    codOriginalDeficiencia = models.IntegerField(blank=True, null=True)


class FatoAluno(models.Model):
    codLocalIESPk = models.ForeignKey('DimLocalIES', models.DO_NOTHING)
    codTempoPk = models.ForeignKey('DimTempo', models.DO_NOTHING)
    codCursoPk = models.ForeignKey('DimCurso', models.DO_NOTHING)
    codReservaVagasPk = models.ForeignKey('DimReservaVagas', models.DO_NOTHING)
    codDeficienciaPk = models.ForeignKey('DimDeficiencia', models.DO_NOTHING)
    codBolsaAuxilioPk = models.ForeignKey('DimBolsaAuxilio', models.DO_NOTHING)

    indiceEscolaPublicaCursosTradicionais = models.IntegerField(blank=True, null=True)
    indiceIngressantesConcluintesRegiaoFederal = models.IntegerField(blank=True, null=True)
    indiceIngressantesConcluintesRegiaoEstadual = models.IntegerField(blank=True, null=True)
    indiceDesistenciaReservaVagasRegiao = models.IntegerField(blank=True, null=True)
    indiceDesistenciaDeficiencia = models.IntegerField(blank=True, null=True)
    indiceConcluintesCapitalInteriorNordeste = models.IntegerField(blank=True, null=True)
    indiceConcluintesBolsistaNordeste = models.IntegerField(blank=True, null=True)
    indiceBaixaRendaNoturnoRegiao = models.IntegerField(blank=True, null=True)
    indiceDesistenciaLicenciaturaIngresso = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = (("codLocalIESPk", "codTempoPk", "codCursoPk", "codReservaVagasPk", "codDeficienciaPk", "codBolsaAuxilioPk"),)

