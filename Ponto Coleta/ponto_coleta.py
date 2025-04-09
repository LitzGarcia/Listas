class PontoDescarte:
    def __init__(self, nome, endereco, material):
        self.nome = nome
        self.endereco = endereco
        self.material = material
        self.proximo = None

def material_presente(material, busca):
    return busca.lower() in material.lower()

def inserir_ponto(lista, nome, endereco, material):
    novo_ponto = PontoDescarte(nome, endereco, material)
    if lista is None:
        return novo_ponto
    else:
        atual = lista
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_ponto
        return lista

def buscar_por_material(lista, busca):
    if lista is None:
        print(f"Nenhum ponto de descarte encontrado para o material: {busca}")
        return
    
    print(f"\nPontos de descarte para o material: {busca}")
    print("-" * 50)
    
    atual = lista
    while atual is not None:
        print(f"Nome: {atual.nome}")
        print(f"Endereço: {atual.endereco}")
        print(f"Materiais aceitos: {atual.material}")
        print("-" * 50)
        atual = atual.proximo 