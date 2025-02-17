import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

class TestFilaAtendimentoProximo(unittest.TestCase):
    def test_CT1_proximo(self):
        """
        CT1 = [1, 2, 3, 5]:
        - Cria uma fila e insere um atendimento.
        - Como a fila não está vazia, o método proximo remove o atendimento e o retorna.
        """
        fila = FilaAtendimento()
        paciente = Paciente(
            nome="Maria Luíza",
            cpf="12345678901",
            email="ct1@example.com",
            nascimento="01/01/2000"
        )
        atendimento = Atendimento(
            paciente=paciente,
            risco=Risco.AMARELO,
            entrada=datetime.now()
        )
        fila.inserir(atendimento)
        
        # CT1: Fila não vazia, deve remover e retornar o atendimento
        resultado = fila.proximo()
        self.assertEqual(resultado.paciente, paciente)

    def test_CT2_proximo(self):
        """
        CT2 = [1, 2, 4]:
        - Cria uma fila vazia.
        - Ao chamar proximo, como a fila está vazia, deve lançar FilaVaziaError.
        """
        fila = FilaAtendimento()
        with self.assertRaises(FilaVaziaError):
            fila.proximo()

if __name__ == '__main__':
    unittest.main(verbosity=2)
