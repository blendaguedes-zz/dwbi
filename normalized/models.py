# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    codigoalunocurso = models.IntegerField(blank=True, null=True)
    codigoaluno = models.BigIntegerField(db_column='codigoAluno', blank=True, null=True)  # Field name made lowercase.
    fkcodigoetnia = models.ForeignKey('Etnia', models.DO_NOTHING, db_column='fkCodigoEtnia', blank=True, null=True)  # Field name made lowercase.
    fkcodigosexo = models.ForeignKey('Sexo', models.DO_NOTHING, db_column='fkCodigosexo', blank=True, null=True)  # Field name made lowercase.
    idadealuno = models.IntegerField(db_column='idadeAluno', blank=True, null=True)  # Field name made lowercase.
    fkcodigosituacao = models.ForeignKey('Situacao', models.DO_NOTHING, db_column='fkCodigoSituacao', blank=True, null=True)  # Field name made lowercase.
    quantidadecargahorariatotal = models.IntegerField(db_column='quantidadeCargahorariaTotal', blank=True, null=True)  # Field name made lowercase.
    quantidadecargahorariaintegral = models.IntegerField(db_column='quantidadeCargaHorariaIntegral', blank=True, null=True)  # Field name made lowercase.
    dataingressocurso = models.CharField(db_column='dataIngressoCurso', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fkcodigoapoiosocial = models.ForeignKey('Apoiosocial', models.DO_NOTHING, db_column='fkCodigoApoioSocial', blank=True, null=True)  # Field name made lowercase.
    inatividadeextracurricular = models.IntegerField(db_column='inatividadeExtraCurricular', blank=True, null=True)  # Field name made lowercase.
    incomplestagio = models.CharField(max_length=10, blank=True, null=True)
    incomplextensao = models.CharField(max_length=10, blank=True, null=True)
    incomplmonitoria = models.CharField(max_length=10, blank=True, null=True)
    incomplpesquisa = models.CharField(max_length=10, blank=True, null=True)
    inbolsaestagio = models.CharField(max_length=10, blank=True, null=True)
    inbolsaextensao = models.CharField(max_length=10, blank=True, null=True)
    inbolsamonitoria = models.CharField(max_length=10, blank=True, null=True)
    inbolsapesquisa = models.CharField(max_length=10, blank=True, null=True)
    codigotipoescolaensinomedio = models.IntegerField(blank=True, null=True)
    inalunoparfor = models.CharField(max_length=10, blank=True, null=True)
    inconcluente = models.IntegerField(blank=True, null=True)
    iningressototal = models.IntegerField(blank=True, null=True)
    iningressovaganova = models.IntegerField(blank=True, null=True)
    anoingresso = models.IntegerField(db_column='anoIngresso', blank=True, null=True)  # Field name made lowercase.
    fkreservavagas = models.ForeignKey('Reservavagas', models.DO_NOTHING, db_column='fkReservaVagas', blank=True, null=True)  # Field name made lowercase.
    fkdeficiencia = models.ForeignKey('Deficiencia', models.DO_NOTHING, db_column='fkDeficiencia', blank=True, null=True)  # Field name made lowercase.
    fkcodigocurso = models.IntegerField(db_column='fkCodigoCurso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aluno'


class Alunocurso(models.Model):
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idaluno', primary_key=True)
    codigocurso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='codigocurso')

    class Meta:
        managed = False
        db_table = 'alunocurso'


class Apoiosocial(models.Model):
    idapoiosocial = models.AutoField(db_column='idApoioSocial', primary_key=True)  # Field name made lowercase.
    alimentacao = models.IntegerField(blank=True, null=True)
    permanencia = models.IntegerField(blank=True, null=True)
    trabalho = models.IntegerField(blank=True, null=True)
    materialdidatico = models.IntegerField(db_column='materialDidatico', blank=True, null=True)  # Field name made lowercase.
    moradia = models.IntegerField(blank=True, null=True)
    transporte = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apoiosocial'


class Categoriaadministrativa(models.Model):
    idcategoriaadministrativa = models.AutoField(db_column='idCategoriaAdministrativa', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoriaAdministrativa'


class Curso(models.Model):
    codigocurso = models.AutoField(primary_key=True)
    fkcodigoies = models.ForeignKey('Ies', models.DO_NOTHING, db_column='fkCodigoIES', blank=True, null=True)  # Field name made lowercase.
    fkcodigotempo = models.ForeignKey('Tempo', models.DO_NOTHING, db_column='fkCodigoTempo', blank=True, null=True)  # Field name made lowercase.
    fkcodigolocaloferta = models.ForeignKey('Local', models.DO_NOTHING, db_column='fkCodigoLocalOferta', blank=True, null=True)  # Field name made lowercase.
    nomecurso = models.CharField(max_length=300, blank=True, null=True)
    incapitalcurso = models.CharField(max_length=68, blank=True, null=True)
    codigomodalidadeensino = models.CharField(max_length=15, blank=True, null=True)
    descricaomodalidadeensio = models.CharField(max_length=29, blank=True, null=True)
    numerocargahoraria = models.CharField(max_length=10, blank=True, null=True)
    codigoturno = models.IntegerField(blank=True, null=True)
    quantidadematriculacurso = models.IntegerField(blank=True, null=True)
    quantidadeconcluintecurso = models.IntegerField(blank=True, null=True)
    quantidadeingressocurso = models.IntegerField(blank=True, null=True)
    quantidadeingressovagasnovas = models.IntegerField(blank=True, null=True)
    fkcodigoturno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='fkCodigoTurno', blank=True, null=True)  # Field name made lowercase.
    fkcodigograuacademico = models.ForeignKey('Grauacademico', models.DO_NOTHING, db_column='fkCodigoGrauAcademico', blank=True, null=True)  # Field name made lowercase.
    codigooriginal = models.IntegerField(db_column='codigoOriginal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso'


class Deficiencia(models.Model):
    iddeficiencia = models.AutoField(db_column='idDeficiencia', primary_key=True)  # Field name made lowercase.
    auditiva = models.IntegerField(blank=True, null=True)
    fisica = models.IntegerField(blank=True, null=True)
    intelectual = models.IntegerField(blank=True, null=True)
    multipla = models.IntegerField(blank=True, null=True)
    surdez = models.IntegerField(blank=True, null=True)
    surdocegueira = models.IntegerField(db_column='surdoCegueira', blank=True, null=True)  # Field name made lowercase.
    baixavisao = models.IntegerField(db_column='baixaVisao', blank=True, null=True)  # Field name made lowercase.
    cegueira = models.IntegerField(blank=True, null=True)
    superdotacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deficiencia'


class Etnia(models.Model):
    codigoetnia = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etnia'


class Grauacademico(models.Model):
    idgrauacademico = models.AutoField(db_column='idGrauAcademico', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grauAcademico'


class Ies(models.Model):
    idcodigoies = models.AutoField(db_column='idCodigoIES', primary_key=True)  # Field name made lowercase.
    nomeies = models.CharField(db_column='nomeIES', max_length=97, blank=True, null=True)  # Field name made lowercase.
    siglaies = models.CharField(db_column='siglaIES', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fkcodigocategoriaadministrativa = models.ForeignKey(Categoriaadministrativa, models.DO_NOTHING, db_column='fkCodigoCategoriaAdministrativa', blank=True, null=True)  # Field name made lowercase.
    fkorganizacaoacademica = models.ForeignKey('Organizacaoacademica', models.DO_NOTHING, db_column='fkOrganizacaoAcademica', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ies'


class Local(models.Model):
    codigolocaloferta = models.AutoField(primary_key=True)
    codigomunicipio = models.IntegerField(blank=True, null=True)
    nomemunicipio = models.CharField(max_length=200, blank=True, null=True)
    codigouf = models.IntegerField(blank=True, null=True)
    siglauf = models.CharField(max_length=2, blank=True, null=True)
    nomeregiao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local'


class Modalidadeensino(models.Model):
    idmodalidadeensino = models.AutoField(db_column='idModalidadeEnsino', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidadeEnsino'


class Organizacaoacademica(models.Model):
    idorganizacaoacademica = models.AutoField(db_column='idOrganizacaoAcademica', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizacaoAcademica'


class Reservavagas(models.Model):
    idreservavagas = models.AutoField(db_column='idReservaVagas', primary_key=True)  # Field name made lowercase.
    deficiencia = models.IntegerField(blank=True, null=True)
    ensinopublico = models.IntegerField(db_column='ensinoPublico', blank=True, null=True)  # Field name made lowercase.
    etnico = models.IntegerField(blank=True, null=True)
    rendafamiliar = models.IntegerField(db_column='rendaFamiliar', blank=True, null=True)  # Field name made lowercase.
    outro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservaVagas'


class Sexo(models.Model):
    codigosexo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sexo'


class Situacao(models.Model):
    codigosituacao = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'situacao'


class Tempo(models.Model):
    codigotempo = models.IntegerField(primary_key=True)
    ano = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempo'


class Turno(models.Model):
    codigoturno = models.AutoField(primary_key=True)
    integral = models.CharField(max_length=1, blank=True, null=True)
    matutino = models.CharField(max_length=1, blank=True, null=True)
    vespertino = models.CharField(max_length=1, blank=True, null=True)
    noturno = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turno'
