import sys

class Veiculo:
    """Representa um veículo com placa, dia e horário."""
    def __init__(self, placa, dia, horario):
        self.placa = placa
        self.dia = dia.upper()
        self.horario = horario

    def __str__(self):
        return f"Placa: {self.placa}, Dia: {self.dia}, Horário: {self.horario}"

def mapear_final_placa_para_dia(final_placa):
    """Mapeia o final da placa para o dia da semana do rodízio."""
    mapa = {
        '1': "SEGUNDA", '2': "SEGUNDA",
        '3': "TERCA", '4': "TERCA",
        '5': "QUARTA", '6': "QUARTA",
        '7': "QUINTA", '8': "QUINTA",
        '9': "SEXTA", '0': "SEXTA"
    }
    return mapa.get(final_placa)

def carregar_dados(criterio, nome_arquivo="dados_veiculos.txt"):
    """Carrega os dados dos veículos do arquivo e filtra pelo critério."""
    veiculos_afetados = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                partes = linha.strip().split()
                if len(partes) == 3:
                    placa, dia_semana, horario = partes
                    veiculo = Veiculo(placa, dia_semana, horario)

                    if criterio.isdigit():
                        final_placa = placa[-1]
                        dia_rodizio = mapear_final_placa_para_dia(final_placa)
                        if final_placa == criterio and dia_rodizio == veiculo.dia:
                           veiculos_afetados.append(veiculo)
                    elif criterio.upper() == veiculo.dia:
                        veiculos_afetados.append(veiculo)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        sys.exit(1)

    return veiculos_afetados

def exibir_veiculos(veiculos):
    """Exibe a lista de veículos."""
    if not veiculos:
        print("Nenhum veículo encontrado para o critério informado.")
        return
    for i, veiculo in enumerate(veiculos):
        print(f"{i + 1}: {veiculo}")

def buscar_veiculos_por_dia(veiculos_filtrados, dia_busca):
    """Busca e exibe veículos para um dia específico dentro da lista já filtrada."""
    encontrados = [v for v in veiculos_filtrados if v.dia == dia_busca.upper()]
    if not encontrados:
        print(f"Nenhum veículo encontrado para {dia_busca.upper()} na lista atual.")
    else:
        print(f"Veículos encontrados para {dia_busca.upper()} na lista atual:")
        exibir_veiculos(encontrados)


def main():
    """Função principal da aplicação."""
    criterio = input("Digite o critério (dia da semana ou final da placa): ").strip()

    veiculos_filtrados = carregar_dados(criterio)

    print("Veículos afetados pelo rodízio (inicial):")
    exibir_veiculos(veiculos_filtrados)

    if not veiculos_filtrados:
        print("Encerrando o programa pois nenhum veículo foi encontrado inicialmente.")
        return

    indice_atual = -1

    while True:
        print("Opções:")
        print("N - Próximo veículo")
        print("B - Buscar por dia da semana (na lista atual)")
        print("S - Sair")
        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == 'N':
            if not veiculos_filtrados:
                print("A lista está vazia.")
                continue
            indice_atual = (indice_atual + 1) % len(veiculos_filtrados)
            print("Veículo atual:")
            print(veiculos_filtrados[indice_atual])
        elif opcao == 'B':
            if not veiculos_filtrados:
                print("A lista está vazia para buscar.")
                continue
            dia = input("Digite o dia da semana para buscar: ").strip()
            buscar_veiculos_por_dia(veiculos_filtrados, dia)
        elif opcao == 'S':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main() 