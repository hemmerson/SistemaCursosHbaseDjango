from django.db import models
from .hbase_config import get_hbase_connection

# Create your models here.
class Professor(models.Model):
    numero_prof = models.CharField(max_length=50, primary_key=True)
    profnome = models.CharField(max_length=100)
    profrua = models.CharField(max_length=200)
    profcidade = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        connection = get_hbase_connection()
        table = connection.table('professor')
        table.put(
            self.numero_prof,
            {
                b'info:profnome': self.profnome.encode(),
                b'info:profrua': self.profrua.encode(),
                b'info:profcidade': self.profcidade.encode()
            }
        )

    @classmethod
    def get(cls, numero_prof):
        connection = get_hbase_connection()
        table = connection.table('professor')
        row = table.row(str(numero_prof))
        if row:
            return cls(
                numero_prof=str(numero_prof),
                profnome=row.get(b'info:profnome', b'').decode(),
                profrua=row.get(b'info:profrua', b'').decode(),
                profcidade=row.get(b'info:profcidade', b'').decode()
            )
        return None

    def delete(self, *args, **kwargs):
        connection = get_hbase_connection()
        table = connection.table('professor')
        table.delete(str(self.numero_prof))

    @classmethod
    def all(cls):
        connection = get_hbase_connection()
        table = connection.table('professor')
        return [
            cls(
                numero_prof=key.decode(),
                profnome=data.get(b'info:profnome', b'').decode(),
                profrua=data.get(b'info:profrua', b'').decode(),
                profcidade=data.get(b'info:profcidade', b'').decode()
            )
            for key, data in table.scan()
        ]

# Model de Aluno ==========================================================================
class Aluno(models.Model):
    numero_aluno = models.CharField(max_length=50, primary_key=True)
    alunome = models.CharField(max_length=100)
    alufrua = models.CharField(max_length=200)
    alucidade = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        connection = get_hbase_connection()
        table = connection.table('aluno')
        table.put(
            self.numero_aluno,
            {
                b'info:alunome': self.alunome.encode(),
                b'info:alufrua': self.alufrua.encode(),
                b'info:alucidade': self.alucidade.encode()
            }
        )

    @classmethod
    def get(cls, numero_aluno):
        connection = get_hbase_connection()
        table = connection.table('aluno')
        row = table.row(str(numero_aluno))
        if row:
            return cls(
                numero_aluno=str(numero_aluno),
                alunome=row.get(b'info:alunome', b'').decode(),
                alufrua=row.get(b'info:alufrua', b'').decode(),
                alucidade=row.get(b'info:alucidade', b'').decode()
            )
        return None

    def delete(self, *args, **kwargs):
        connection = get_hbase_connection()
        table = connection.table('aluno')
        table.delete(str(self.numero_aluno))

    @classmethod
    def all(cls):
        connection = get_hbase_connection()
        table = connection.table('aluno')
        return [
            cls(
                numero_aluno=key.decode(),
                alunome=data.get(b'info:alunome', b'').decode(),
                alufrua=data.get(b'info:alufrua', b'').decode(),
                alucidade=data.get(b'info:alucidade', b'').decode()
            )
            for key, data in table.scan()
        ]

# Model de Disciplina =====================================================================
class Disciplina(models.Model):
    codigo_disc = models.CharField(max_length=50, primary_key=True)
    nome_disciplina = models.CharField(max_length=100)
    nome_curso = models.CharField(max_length=100)
    qtd_aulas = models.IntegerField()

    def save(self, *args, **kwargs):
        connection = get_hbase_connection()
        table = connection.table('disciplina')
        table.put(
            self.codigo_disc,
            {
                b'info:nome_disciplina': self.nome_disciplina.encode(),
                b'info:nome_curso': self.nome_curso.encode(),
                b'info:qtd_aulas': str(self.qtd_aulas).encode()
            }
        )

    @classmethod
    def get(cls, codigo_disc):
        connection = get_hbase_connection()
        table = connection.table('disciplina')
        row = table.row(str(codigo_disc))
        if row:
            return cls(
                codigo_disc=str(codigo_disc),
                nome_disciplina=row.get(b'info:nome_disciplina', b'').decode(),
                nome_curso=row.get(b'info:nome_curso', b'').decode(),
                qtd_aulas=int(row.get(b'info:qtd_aulas', b'').decode())
            )
        return None

    def delete(self, *args, **kwargs):
        connection = get_hbase_connection()
        table = connection.table('disciplina')
        table.delete(str(self.codigo_disc))

    @classmethod
    def all(cls):
        connection = get_hbase_connection()
        table = connection.table('disciplina')
        return [
            cls(
                codigo_disc=key.decode(),
                nome_disciplina=data.get(b'info:nome_disciplina', b'').decode(),
                nome_curso=data.get(b'info:nome_curso', b'').decode(),
                qtd_aulas=int(data.get(b'info:qtd_aulas', b'0').decode())
            )
            for key, data in table.scan()
        ]

# Model de Matricula ======================================================================
class Matricula:
    def __init__(self, numero_aluno, codigo_disc, ano):
        self.numero_aluno = numero_aluno
        self.codigo_disc = codigo_disc
        self.ano = ano

    def save(self):
        connection = get_hbase_connection()
        table = connection.table('matricula')
        table.put(
            f"{self.numero_aluno}#{self.codigo_disc}#{self.ano}".encode(),
            {
                b'info:ano': self.ano.encode()
            }
        )

    @staticmethod
    def get(numero_aluno, codigo_disc, ano):
        connection = get_hbase_connection()
        table = connection.table('matricula')
        row = table.row(f"{numero_aluno}#{codigo_disc}#{ano}".encode())
        if row:
            return Matricula(
                numero_aluno=numero_aluno,
                codigo_disc=codigo_disc,
                ano=row.get(b'info:ano').decode()
            )
        return None

    def delete(self):
        connection = get_hbase_connection()
        table = connection.table('matricula')
        table.delete(f"{self.numero_aluno}#{self.codigo_disc}#{self.ano}".encode())

    @staticmethod
    def all():
        connection = get_hbase_connection()
        table = connection.table('matricula')
        matriculas = []
        for key, data in table.scan():
            parts = key.decode().split('#')
            if len(parts) == 3:
                matriculas.append(Matricula(
                    numero_aluno=parts[0],
                    codigo_disc=parts[1],
                    ano=data.get(b'info:ano', b'').decode()
                ))
        return matriculas

# Model de ProfDisc =======================================================================
class ProfDisc:
    def __init__(self, codigo_disc, numero_prof, ano):
        self.codigo_disc = codigo_disc
        self.numero_prof = numero_prof
        self.ano = ano

    def save(self):
        connection = get_hbase_connection()
        table = connection.table('profdisc')
        table.put(
            f"{self.codigo_disc}#{self.numero_prof}#{self.ano}".encode(),
            {
                b'info:ano': self.ano.encode()
            }
        )

    @staticmethod
    def get(codigo_disc, numero_prof, ano):
        connection = get_hbase_connection()
        table = connection.table('profdisc')
        row = table.row(f"{codigo_disc}#{numero_prof}#{ano}".encode())
        if row:
            return ProfDisc(
                codigo_disc=codigo_disc,
                numero_prof=numero_prof,
                ano=row.get(b'info:ano').decode()
            )
        return None

    def delete(self):
        connection = get_hbase_connection()
        table = connection.table('profdisc')
        table.delete(f"{self.codigo_disc}#{self.numero_prof}#{self.ano}".encode())

    @staticmethod
    def all():
        connection = get_hbase_connection()
        table = connection.table('profdisc')
        profdiscs = []
        for key, data in table.scan():
            parts = key.decode().split('#')
            if len(parts) == 3:
                profdiscs.append(ProfDisc(
                    codigo_disc=parts[0],
                    numero_prof=parts[1],
                    ano=data.get(b'info:ano', b'').decode()
                ))
        return profdiscs