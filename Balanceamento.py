import unittest


class PilhaVazia(Exception):
    pass

class Pilha():
    def __init__(self):
        self.lista = []

    def vazia(self):
        return len(self.lista) == 0

    def topo(self):
        if self.vazia():
            raise PilhaVazia
        else:
            return self.lista[-1]

    def empilhar(self, valor):
        self.lista.append(valor)

    def desempilhar(self):
        if self.vazia():
            raise PilhaVazia
        return self.lista.pop()

def esta_balanceada(expressao):
    """
    O tempo de execução deste programa esta em O(n)

    O espaço de memória ocupado está em O(n)
    """
    if len(expressao) == 0:
        return True
    elif len(expressao) == 1 or expressao[0] == ')' or expressao [0] == ']' or expressao[0] == '}':
        return False
    verificar = Pilha()
    for x in expressao:
        if x == '(' or x == '[' or x == '{':
            verificar.empilhar(x)
        elif x == ')' or x == ']' or x == '}':
            if x == ')' and verificar.desempilhar()!= '(':
                return False
            elif x== ']' and verificar.desempilhar()!= '[':
                return False
            elif x == '}' and verificar.desempilhar()!='{':
                return False
    if len(verificar.lista)%2!=0:
        return False
    return True

class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))
