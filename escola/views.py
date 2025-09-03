from escola.models import Estudante,Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Exibe todas os estudantes com suas respectivas informações! Possui também um CRUD do mesmo!
    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.
    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.
    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    Parâmetros:
    - pk (int): O identificador primário do objeto, ou também a chave primária. Deve ser um número inteiro.
    """
    queryset = Estudante.objects.all().order_by("id")
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Exibe todas os cursos
    Parâmetros:
    - pk (int): O identificador primário do objeto, ou também a chave primária. Deve ser um número inteiro.
    """
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Exibe todas as matriculas por estudante além de possuir um CRUD do mesmo!
    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    Parâmetros:
    - pk (int): O identificador primário do objeto, ou também a chave primária. Deve ser um número inteiro.
    """
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]
class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista matriculas por ID do estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto, ou também a chave primária. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista matriculas por ID do curso
    Parâmetros:
    - pk (int): O identificador primário do objeto, ou também a chave primária. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasCursoSerializer