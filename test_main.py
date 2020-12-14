"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_maior(self):
        """Função que testa se o primeiro é maior."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['1', '0']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            nums = list(map(float, input_returns))
            assert mock_input.call_count == 2
            mock_print.assert_called_with('1.0')

    def test_menor(self):
        """Função que testa se o segundo é maior."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['0', '1']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            mock_print.assert_called_with('1.0')


if __name__ == '__main__':
    unittest.main()
