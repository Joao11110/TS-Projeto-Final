import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise
from main.cli import TerminalClient
from main.service import ProntoSocorroService
import io
import sys

# Classes auxiliares para simular o serviço do Pronto-Socorro

class DummyPaciente:
    def __init__(self, nome, cpf, email, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.nascimento = nascimento
    def __str__(self):
        return f"Paciente({self.nome})"

class FakePacientes:
    def buscar(self, cpf):
        # Se o CPF for "123", retorna um paciente dummy; caso contrário, retorna None.
        if cpf == "123":
            return DummyPaciente("Dummy Paciente", "123", "dummy@example.com", "01/01/2000")
        return None

class FakeProntoSocorroService:
    def __init__(self):
        self.pacientes = FakePacientes()
    def registrar_paciente(self, nome, cpf, email, nascimento):
        # Retorna um paciente dummy usando os dados informados.
        return DummyPaciente(nome, cpf, email, nascimento)
    def registrar_atendimento(self, paciente, risco):
        return "Dummy Atendimento"
    def inserir_fila_atendimento(self, atendimento):
        # Apenas simula a inserção; não faz nada.
        pass
    def chamar_proximo(self):
        return "Dummy Próximo"
    def buscar_historico(self, paciente):
        return ["Atendimento 1", "Atendimento 2"]
    def classificar_risco(self, ficha):
        # Retorna um objeto dummy com atributo 'name'
        class DummyRisco:
            name = "DummyRisco"
        return DummyRisco()

# Testes para o método executar da TerminalClient
class TestTerminalClientExecutar(unittest.TestCase):

    @patch('builtins.input')
    def test_CT1_executar(self, mock_input):
        """
        CT1 = [1,2,3,4,5,7,9,11,13,14] conforme o grafo:
          Iteração 1: opção "1" → registrar_paciente()
          Iteração 2: opção "2" → registrar_atendimento()
          Iteração 3: opção "3" → chamar_proximo()
          Iteração 4: opção "4" → buscar_historico()
          Iteração 5: opção "5" → sair do sistema
          
        As entradas adicionais para os métodos são simuladas na sequência:
          - Registrar Paciente: Nome, CPF, E-mail, Nascimento
          - Registrar Atendimento: CPF, e depois respostas para as perguntas de triagem
          - Buscar Histórico: CPF
        """
        # Sequência de entradas:
        # Iteração 1 (Registrar Paciente):
        #   "1" (menu), depois: "Teste Paciente", "12345678901", "teste@ex.com", "01/01/2000"
        # Iteração 2 (Registrar Atendimento):
        #   "2" (menu), depois: "123", "sim", "sim", "não", "não"
        # Iteração 3 (Chamar Próximo):
        #   "3" (menu)
        # Iteração 4 (Buscar Histórico):
        #   "4" (menu), depois: "123"
        # Iteração 5 (Sair):
        #   "5" (menu)
        entradas = [
            "1", "Teste Paciente", "12345678901", "teste@ex.com", "01/01/2000",
            "2", "123", "sim", "sim", "não", "não",
            "3",
            "4", "123",
            "5"
        ]
        mock_input.side_effect = entradas

        # Capturar a saída para verificarmos se os métodos foram chamados corretamente
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Instanciar TerminalClient com o serviço fake
        fake_service = FakeProntoSocorroService()
        client = TerminalClient(fake_service)
        client.executar()

        # Restaurar stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        # Verificamos se as mensagens dos métodos dummy aparecem na saída
        self.assertIn("Paciente registrado com sucesso", output)
        self.assertIn("Classificação de risco:", output)
        self.assertIn("Atendimento registrado e inserido na fila", output)
        self.assertIn("Próximo Paciente", output)
        self.assertIn("Histórico de atendimentos para", output)
        self.assertIn("Saindo do sistema", output)

    @patch('builtins.input')
    def test_CT2_executar(self, mock_input):
        """
        CT2 = [1,2,3,4,5,7,9,11,13,15,16,2,3,4,5,7,9,11,13,14]
        Neste cenário:
          Iteração 1: entrada inválida "7" → deve imprimir "Opção inválida, tente novamente."
          Iteração 2: entrada "5" → sair do sistema.
        """
        # Sequência de entradas para CT2:
        entradas = ["7", "5"]
        mock_input.side_effect = entradas

        captured_output = io.StringIO()
        sys.stdout = captured_output

        fake_service = FakeProntoSocorroService()
        client = TerminalClient(fake_service)
        client.executar()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        # Verifica se a mensagem de opção inválida está presente
        self.assertIn("Opção inválida, tente novamente.", output)
        self.assertIn("Saindo do sistema", output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
