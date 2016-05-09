#!-*- conding: utf8 -*-
#coding: utf-8

from collections import Counter

dicionario_quadrados_perfeitos = {}
maior_chave = 0

def monta_dicionario(n):
    global maior_chave
    if maior_chave <= n:
        chave = maior_chave
        while (chave * chave) <= n:
            dicionario_quadrados_perfeitos[chave*chave] = 0
            chave+=1
            maior_chave = chave
    return dicionario_quadrados_perfeitos

def soma_quadrados(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    else:
        dicionario_menores_quadrados = monta_dicionario(n)

        lista_de_chaves = list(dicionario_menores_quadrados)
        lista_de_chaves.sort()
        lista_de_chaves.remove(0)

        lista_de_possibilidades = []
        possibilidade = []
        soma = 0
        posicao_da_lista = len(lista_de_chaves)-1
        aux_posicao = posicao_da_lista
        while True:
            if lista_de_chaves[posicao_da_lista] <= n and soma < n :
                if soma + lista_de_chaves[posicao_da_lista] > n:
                    posicao_da_lista-=1
                else:
                    soma+=lista_de_chaves[posicao_da_lista]
                    possibilidade.append(lista_de_chaves[posicao_da_lista])
            elif soma == n:
                if possibilidade in lista_de_possibilidades:
                    break
                lista_de_possibilidades.append(possibilidade)
                possibilidade = []
                soma = 0
                aux_posicao -=1
                posicao_da_lista = aux_posicao
            else:
                posicao_da_lista-=1


        ultimo_tamanho = len(lista_de_possibilidades[0])
        for lista in lista_de_possibilidades:
            if len(lista) < ultimo_tamanho:
                ultimo_tamanho = len(lista)
                possibilidade = lista

    return possibilidade

import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
