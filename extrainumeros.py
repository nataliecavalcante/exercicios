def extrair_nomes(lista_objetos):
    nomes = []
    for obj in lista_objetos:
        nomes.append(obj.nome)
    return nomes
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# Criando alguns objetos
p1 = Pessoa("Alice")
p2 = Pessoa("Bruno")
p3 = Pessoa("Carla")

lista_pessoas = [p1, p2, p3]

# Usando a função
nomes = extrair_nomes(lista_pessoas)
print(nomes)