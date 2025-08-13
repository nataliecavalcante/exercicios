def contar_ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador
lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
valor = 2

resultado = contar_ocorrencias(lista, valor)
print(f"O valor {valor} aparece {resultado} vezes na lista.")