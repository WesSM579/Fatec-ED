# A função min_max deverá rodar em O(n) e o código não pode usar nenhuma
# lib do Python (sort, min, max e etc)
# Não pode usar qualquer laço (while, for), a função deve ser recursiva
# Ou delegar a solução para uma função puramente recursiva
import unittest

def max_min_recursivo(seq,cursor,max,min):
    if cursor == len(seq):
        return min, max
    elemento_atual = seq[cursor]
    if elemento_atual > max:
        max = elemento_atual
    if elemento_atual < min:
        min = elemento_atual
    return max_min_recursivo(seq,cursor+1,max,min)
def min_max(seq):
    '''
    :param seq: uma sequencia
    :return: (min, max)
    Retorna tupla cujo primeiro valor mínimo (min) é o valor
    mínimo da sequencia seq.
    O segundo é o valor máximo (max) da sequencia
    '''
    if seq:
        return max_min_recursivo(seq,1,seq[0],seq[0])
    return None, None


class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))

    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()
