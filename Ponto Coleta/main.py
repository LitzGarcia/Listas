import locale
from ponto_coleta import PontoDescarte, material_presente, inserir_ponto, buscar_por_material

def main():
    locale.setlocale(locale.LC_ALL, 'Portuguese')
    
    try:
        with open('pontos_de_descartes.txt', 'r', encoding='utf-8') as arquivo:
            lista = None
            
            busca = input("Digite o tipo de material para buscar (ex: Plastico, Vidro, Eletronicos): ")
            
            for linha in arquivo:
                dados = linha.strip().split(';')
                if len(dados) == 3:
                    nome, endereco, material = dados
                    if material_presente(material, busca):
                        lista = inserir_ponto(lista, nome, endereco, material)
            
            buscar_por_material(lista, busca)
            
            atual = lista
            while atual:
                temp = atual
                atual = atual.proximo
                del temp
                
    except FileNotFoundError:
        print("Erro ao abrir o arquivo!")
        return 1
    
    return 0

if __name__ == "__main__":
    main() 