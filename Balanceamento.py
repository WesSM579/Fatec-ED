import unittest

class Pilha():
    def __init__(self):
        self.lista=[]

    def vazia(self):
        return len(self.lista)==0

    def topo(self):
        if len(self.lista)==0:
            raise IndexError
        else:
            return self.lista[-1]

    def empilhar(self,valor):
        self.lista.append(valor)

    def desempilhar(self):
        if len(self.lista)==0:
            raise IndexError
        else:
            return self.lista.pop()

def esta_balanceada(expressao):
    chave=Pilha()
    parentese=Pilha()
    colchete=Pilha()
    for letra in expressao:
        if letra == '(':
            parentese.empilhar(0)
        if letra =='{':
            chave.empilhar(0)
        if letra=='[':
            colchete.empilhar(0)
        if letra == ')':
            try:
                parentese.desempilhar()
            except IndexError:
                return False
        if letra == ']':
            try:
                colchete.desempilhar()
            except IndexError:
                return False
        if letra == '}':
            try:
                chave.desempilhar()
            except IndexError:
                return False
    if chave.vazia() and parentese.vazia() and colchete.vazia():
        return True
    else:
        return False
    """
    Tempo de execução O(n), pois vai percorrer um for por toda a expressao
    O(n) para memória pois as pilhas crescem de tamanho conforme aumenta a expressao
    """
    pass


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
    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))

if __name__ == '__main__':
    unittest.main()
