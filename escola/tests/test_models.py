from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #    self.fail("Teste de falha intencional para verificar o funcionamento do framework de testes.")
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='João Silva',
            email='testemodel@gmail.com',
            cpf='70198525052',
            data_nascimento='2005-05-15',
            celular='11 98765-4321'
        )

    def test_verifica_atributos_de_estudante(self):
        """Verifica se os atributos do estudante foram definidos corretamente."""
        self.assertEqual(self.estudante.nome, 'João Silva')
        self.assertEqual(self.estudante.email, 'testemodel@gmail.com') 
        self.assertEqual(self.estudante.cpf, '70198525052')
        self.assertEqual(self.estudante.data_nascimento, '2005-05-15')
        self.assertEqual(self.estudante.celular, '11 98765-4321')

class ModelCursoTestCase(TestCase):

    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CTM',
            descricao = 'Curso Teste Modelo',
            nivel = 'A'
        )

    def test_verifica_atributos_de_curso(self):
        """Verifica se os atributos do curso foram definidos corretamente."""
        self.assertEqual(self.curso.codigo, 'CTM')
        self.assertEqual(self.curso.descricao, 'Curso Teste Modelo')
        self.assertEqual(self.curso.nivel, 'A')

class ModelMatriculaTestCase(TestCase):
    
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')