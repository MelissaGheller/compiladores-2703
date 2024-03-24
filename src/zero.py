# SPDX-License-Identifer: MIT

def procura_maior(lista):
    maior = lista[0]
    for item in lista[1:]:
        if item > maior:
            maior = item
    return maior

def procura_menor(dados: list) -> int:
    menor = dados[0]
    for item in dados[1:]:
        if item < menor:
            menor = item
    return menor