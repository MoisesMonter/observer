'''Padrão Observer - Permite que um objeto notifique uma lista de objetos dependentes.'''

'''Interface Observador'''
class Observador:
    def atualizar(self, dados):
        pass

''' Observador Concreto 1 '''
class ObservadorConcreto1(Observador):
    def atualizar(self, dados):
        print(f"Observador 1: Recebeu a atualização com os dados {dados}")

''' Observador Concreto 2 '''
class ObservadorConcreto2(Observador):
    def atualizar(self, dados):
        print(f"Observador 2: Recebeu a atualização com os dados {dados}")

''' Sujeito/Objeto Observado'''
class ObjetoObservado:
    def __init__(self):
        self._observadores = []
        self._dados = None

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.atualizar(self._dados)

    def definir_dados(self, dados):
        self._dados = dados
        self.notificar_observadores()

''' Exemplo de Uso'''
if __name__ == "__main__":
    objeto_observado = ObjetoObservado()

    observador1 = ObservadorConcreto1()
    observador2 = ObservadorConcreto2()

    objeto_observado.adicionar_observador(observador1)
    objeto_observado.adicionar_observador(observador2)

    objeto_observado.definir_dados("Mudança 1")
    objeto_observado.remover_observador(observador1)

    objeto_observado.definir_dados("Mudança 2")
