from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, _categoria):
        self._nome = nome.title()
        self.categoria = _categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(25)} | {restaurante._ativo}')
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente ,nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)    
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas,1)
        return media 