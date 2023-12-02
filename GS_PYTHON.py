import random

def consultar_sintomas():
    # Definição dos sintomas e suas relações com doenças
    sintomas_disponiveis = {
        "febre": ["Resfriado", "Gripe", "Dengue"],
        "tosse": ["Resfriado", "Gripe", "Bronquite"],
        "dor_de_cabeca": ["Resfriado", "Enxaqueca", "Gripe"],
        "dor_de_garganta": ["Resfriado", "Gripe", "Amigdalite"],
        "cansaco": ["Gripe", "Anemia", "Hipotireoidismo"],
        "nariz_entupido": ["Resfriado", "Sinusite", "Gripe"],
        "dor_no_corpo": ["Gripe", "Dengue", "Fibromialgia"],
        "vomito": ["Gripe", "Intoxicação", "Enxaqueca"],
        "diarreia": ["Gastroenterite", "Intoxicação", "Síndrome do Intestino Irritável"],
        "dor_nas_articulacoes": ["Gripe", "Artrite", "Dengue"]
    }

    print("Lista de sintomas disponíveis:")
    for sintoma in sintomas_disponiveis.keys():
        print(f"- {sintoma}")

    # Validando a quantidade de sintomas
    num_sintomas = input("Quantos sintomas você vai digitar (1 a 3)? ")
    while not num_sintomas.isdigit() or not 1 <= int(num_sintomas) <= 3:
        print("Resposta inválida. Por favor, digite novamente!!")
        num_sintomas = input("Quantos sintomas você vai digitar (1 a 3)? ")

    num_sintomas = int(num_sintomas)

    sintomas_usuario = []
    for _ in range(num_sintomas):
        sintoma = input("Digite um sintoma: ").lower()
        while sintoma not in sintomas_disponiveis:
            print("Sintoma não reconhecido. Por favor, escolha um sintoma válido.")
            sintoma = input("Digite um sintoma: ").lower()
        sintomas_usuario.append(sintoma)

    # Verificando a doença mais provável com base nos sintomas do usuário
    contagem_doencas = {}
    for sintoma in sintomas_usuario:
        for doenca in sintomas_disponiveis[sintoma]:
            contagem_doencas[doenca] = contagem_doencas.get(doenca, 0) + 1

    # Ordenando as doenças por contagem (doença mais provável primeiro)
    doencas_ordenadas = sorted(contagem_doencas.items(), key=lambda x: x[1], reverse=True)

    print("\nRelação de doenças mais prováveis:")
    for doenca, contagem in doencas_ordenadas:
        print(f"{doenca}: {contagem} sintomas")

    # Selecionando a doença mais provável
    doenca_mais_provavel = doencas_ordenadas[0][0]

    # Identificando a área médica relacionada à doença mais provável
    area_medica = identificar_area_medica(doenca_mais_provavel)

    # Perguntando a região onde o usuário mora
    regiao = input("Em qual região você mora (norte, sul, leste ou oeste)? ").lower()
    while regiao not in ["norte", "sul", "leste", "oeste"]:
        print("Resposta inválida. Por favor, digite novamente!!")
        regiao = input("Em qual região você mora (norte, sul, leste ou oeste)? ").lower()

    # Obtendo a lista de hospitais e convênios correspondentes à região
    hospitais, convenios = obter_hospitais_e_convenios(regiao)

    # Perguntando ao usuário sobre o convênio
    conv = input("Qual é o seu convênio (verde, amarelo ou azul)? ").lower()
    while conv not in convenios:
        print("Resposta inválida. Por favor, digite novamente!!")
        conv = input("Qual é o seu convênio (verde, amarelo ou azul)? ").lower()

    # Selecionando aleatoriamente o doutor e o dia da semana
    doutor = random.choice(["Dr. Silva", "Dra. Santos", "Dr. Lima", "Dra. Oliveira", "Dr. Almeida"])
    dia_semana = random.choice(["segunda, quarta e sexta", "terça e quinta", "sábado e domingo"])

    # Adicionando endereços fictícios aos hospitais
    hospitais_enderecos = {
        "Hospital A": "Rua 1, 123 - Zona Norte",
        "Hospital B": "Avenida 7, 456 - Zona Norte",
        "Hospital C": "Rua 2, 789 - Zona Norte",
        "Hospital D": "Avenida 8, 111 - Zona Sul",
        "Hospital F": "Rua 3, 222 - Zona Sul",
        "Hospital G": "Avenida 9, 333 - Zona Sul",
        "Hospital H": "Rua 4, 444 - Zona Leste",
        "Hospital I": "Avenida 10, 555 - Zona Leste",
        "Hospital J": "Rua 5, 666 - Zona Leste",
        "Hospital K": "Avenida 11, 777 - Zona Oeste",
        "Hospital L": "Rua 6, 888 - Zona Oeste",
        "Hospital M": "Avenida 12, 999 - Zona Oeste",
    }

    endereco_hospital = hospitais_enderecos[random.choice(hospitais)]

    # Exibindo informações finais para o usuário
    print("\nInformações Finais:")
    print(f"Doença mais provável: {doenca_mais_provavel}")
    print(f"Área médica responsável: {area_medica}")
    print(f"Hospital recomendado: {random.choice(hospitais)}")
    print(f"Endereço do hospital: {endereco_hospital}")
    print(f"Convênio: {conv}")
    print(f"Doutor disponível: {doutor}")
    print(f"Atendimento nos dias: {dia_semana}")

def identificar_area_medica(doenca):
    # Função para identificar a área médica relacionada à doença
    # (Esta é uma implementação fictícia, você pode ajustá-la conforme necessário)
    if "Resfriado" in doenca or "Gripe" in doenca:
        return "Clínica Geral"
    elif "Dengue" in doenca or "Fibromialgia" in doenca:
        return "Reumatologia"
    elif "Bronquite" in doenca or "Amigdalite" in doenca:
        return "Pneumologia"
    elif "Anemia" in doenca or "Hipotireoidismo" in doenca:
        return "Hematologia"
    elif "Sinusite" in doenca or "Enxaqueca" in doenca:
        return "Otorrinolaringologia"
    elif "Intoxicação" in doenca or "Síndrome do Intestino Irritável" in doenca:
        return "Gastroenterologia"
    elif "Artrite" in doenca:
        return "Reumatologia"
    else:
        return "Área Médica Desconhecida"

def obter_hospitais_e_convenios(regiao):
    # Função para obter hospitais e convenios com base na região
    if regiao == "norte":
        hospitais = ["Hospital A", "Hospital B", "Hospital C"]
        convenios = ["verde", "amarelo", "azul"]
    elif regiao == "sul":
        hospitais = ["Hospital D", "Hospital F", "Hospital G"]
        convenios = ["verde", "amarelo", "azul"]
    elif regiao == "leste":
        hospitais = ["Hospital H", "Hospital I", "Hospital J"]
        convenios = ["verde", "amarelo", "azul"]
    elif regiao == "oeste":
        hospitais = ["Hospital K", "Hospital L", "Hospital M"]
        convenios = ["verde", "amarelo", "azul"]
    else:
        hospitais = []
        convenios = []
    return hospitais, convenios

# Exemplo de uso
consultar_sintomas()