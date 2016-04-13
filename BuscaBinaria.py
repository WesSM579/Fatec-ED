#!-*- coding: utf8 -*-
#coding: utf-8

def busca_binaria(seq, procurado):
    """
    Complexidade: O(n) para tempo de execução e O(1) para espaço em memória
    """
    seq.sort()
    inicio=0
    fim=len(seq)-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if procurado > seq[meio]:
            inicio = meio + 1
        elif procurado<seq[meio]:
            fim = meio-1
        else:
            while meio > 0 and seq[meio] == seq[meio-1]:
                meio-=1
            return meio
    return inicio
import unittest

class BuscaBinariaTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertEqual(0, busca_binaria([], 1))
        self.assertEqual(0, busca_binaria([], 2))
        self.assertEqual(0, busca_binaria([], 3))

    def teste_lista_unitaria(self):
        self.assertEqual(0, busca_binaria([1], 0))
        self.assertEqual(0, busca_binaria([1], 1))
        self.assertEqual(1, busca_binaria([1], 2))
        self.assertEqual(1, busca_binaria([1], 3))
        self.assertEqual(1, busca_binaria([1], 4))

    def teste_lista_nao_unitaria(self):
        lista = list(range(10))
        self.assertEqual(0, busca_binaria(lista, -2))
        self.assertEqual(0, busca_binaria(lista, -1))
        for i in lista:
            self.assertEqual(i, busca_binaria(lista, i))
        self.assertEqual(10, busca_binaria(lista, 10))
        self.assertEqual(10, busca_binaria(lista, 11))
        self.assertEqual(10, busca_binaria(lista, 12))

    def teste_lista_elementos_repetidos(self):
        lista = [0, 0, 1, 1, 1, 2, 2, 2]
        self.assertEqual(2, busca_binaria(lista, 1))
        self.assertEqual(5, busca_binaria(lista, 2))

    def teste_lista_elementos_desordenados(self):
        lista = [2, 11, 1, 10, 0, 2, 2, 1, 1, 1]
        self.assertEqual(1, busca_binaria(lista, 1))
        self.assertEqual(5, busca_binaria(lista, 2))
        self.assertEqual(8, busca_binaria(lista, 5))
