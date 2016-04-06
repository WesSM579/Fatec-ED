#!-*- conding: utf8 -*-
#coding: utf-8
import unittest
def _quick_recursivo(seq, inicio, final):
    if inicio >= final:
        return seq
    indice_pivot = final
    pivot = seq[indice_pivot]
    i_esquerda = inicio
    i_direita = final - 1

    #posicionando pivot
    while i_esquerda <= i_direita:

        while seq[i_direita] >= pivot and i_esquerda <= i_direita:
            i_direita -= 1

        while seq[i_esquerda] <= pivot and i_esquerda <= i_direita:
            i_esquerda += 1

        if i_direita > i_esquerda:
            seq[i_direita], seq[i_esquerda] = seq[i_esquerda], seq[i_direita]

    _fim = i_esquerda - 1
    _inicio = i_esquerda + 1
    seq[final], seq[i_esquerda] = seq[i_esquerda], seq[final]

     # Resolvendo para sublista da esquerda
    _quick_recursivo(seq, inicio, _fim)

     # Resolvendo para sublista da direita
    _quick_recursivo(seq, _inicio, final)

    return seq


def quick_sort(seq):
    '''
    Análise de Complexidade: O(n)² para o pior caso e o(n) * log(n) para o melhor caso, para a memória log(n)
    '''
    return _quick_recursivo(seq, 0, len(seq) - 1)

def quick_sort(seq):
    return _quick_recursivo(seq, 0, len(seq) - 1)

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_com_elementos_repetidos(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0, 9, 9]))

    def teste_lista_so_com_elementos_repetidos(self):
        self.assertListEqual([9, 9, 9], quick_sort([9, 9, 9]))
