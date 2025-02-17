import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

class TestFilaAtendimentoInserir(unittest.TestCase):
    """
    Grafo - Classe FilaAtendimento - método inserir
    
    Nós:
    1: início
    2: preparar tupla
    3: heapq.heappush
    4: fim

    CT1 = [1, 2, 3, 4]
    Fluxo completo de inserção sem ramificações:
    - Início -> preparar tupla -> heapq.heappush -> fim
    """

    def test_CT1_inserir(self):
        """
        Verifica se o método inserir percorre o caminho [1, 2, 3, 4] com sucesso.
        - Cria uma fila vazia.
        - Cria um atendimento válido.
        - Chama inserir e verifica se o atendimento foi adicionado.
        """
        fila = FilaAtendimento()
        paciente = Paciente(
            nome="José",
            cpf="12345678901",
            email="teste@example.com",
            nascimento="01/01/2000"
        )
        atendimento = Atendimento(
            paciente=paciente,
            risco=Risco.AMARELO,
            entrada=datetime.now()
        )

        fila.inserir(atendimento)
        self.assertEqual(fila.tamanho(), 1, "A fila deve conter 1 atendimento após a inserção.")

if __name__ == '__main__':
    unittest.main(verbosity=2)