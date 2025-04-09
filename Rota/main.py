import sys

class Rota:
    """Representa uma rota de transporte (formato ID;Nome;Tipo;Regiao)."""
    def __init__(self, id_rota, nome, tipo, regiao):
        self.id_rota = int(id_rota)
        self.nome = nome
        self.tipo = tipo
        self.regiao = regiao

    def __str__(self):
        """Retorna uma representação em string da rota."""
        return f"ID: {self.id_rota}, Nome: {self.nome}, Tipo: {self.tipo}, Região: {self.regiao}"

    def __lt__(self, other):
        """Define a ordem alfabética baseada no nome para ordenação."""
        return self.nome.lower() < other.nome.lower()

def carregar_rotas_de_arquivo(nome_arquivo, filtro):
    """Carrega rotas de um arquivo, filtra por tipo ou região e ordena por nome."""
    rotas = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    partes = linha.split(';')
                    if len(partes) == 4:
                        id_rota_str, nome, tipo, regiao = partes
                        if filtro.lower() in nome.lower() or \
                           filtro.lower() in tipo.lower() or \
                           filtro.lower() in regiao.lower():
                            rota = Rota(id_rota_str, nome, tipo, regiao)
                            rotas.append(rota)
                    else:
                        print(f"Aviso: Linha ignorada por formato inválido: {linha}", file=sys.stderr)
                except ValueError:
                    print(f"Aviso: Linha ignorada por dados inválidos (ID não numérico?): {linha}", file=sys.stderr)
                except Exception as e:
                    print(f"Aviso: Erro ao processar linha '{linha}': {e}", file=sys.stderr)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo '{nome_arquivo}': {e}", file=sys.stderr)
        return []

    rotas.sort()
    return rotas

def exibir_lista_em_ordem(lista_rotas):
    """Exibe as rotas da lista em ordem (alfabética por nome)."""
    if not lista_rotas:
        print("Nenhuma rota encontrada para o filtro especificado.")
        return
    for rota in lista_rotas:
        print(rota)

def exibir_lista_em_ordem_inversa(lista_rotas):
    """Exibe as rotas da lista em ordem inversa (alfabética por nome)."""
    if not lista_rotas:
        return
    for rota in reversed(lista_rotas):
        print(rota)

def main():
    """Função principal da aplicação."""
    print("========================================================")
    filtro = input("Informe o tipo de transporte/região desejada: ")
    print("========================================================")

    lista_rotas = carregar_rotas_de_arquivo("rotas_de_transportes.txt", filtro)

    print("========================================================")
    print("Rotas em ordem (por nome):")
    exibir_lista_em_ordem(lista_rotas)
    print("========================================================")
    print("Rotas em ordem inversa (por nome):")
    exibir_lista_em_ordem_inversa(lista_rotas)
    print("========================================================")

if __name__ == "__main__":
    main() 