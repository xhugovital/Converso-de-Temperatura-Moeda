# === CONVERSOR DE TEMPERATURA E MOEDA ===
# Estrutura modular e organizada

# Taxas fixas (30/03/2026)
TAXAS_CAMBIO = {
    ("USD", "BRL"): 5.25,
    ("BRL", "USD"): 0.19,
    ("EUR", "BRL"): 6.01,
    ("BRL", "EUR"): 0.17,
    ("USD", "EUR"): 0.92,
    ("EUR", "USD"): 1.09
}

def converter_temperatura(valor, origem, destino):
    if origem == "C" and destino == "F":
        return (valor * 9/5) + 32
    elif origem == "F" and destino == "C":
        return (valor - 32) * 5/9
    return None

def converter_moeda(valor, origem, destino):
    chave = (origem, destino)
    if chave in TAXAS_CAMBIO:
        return valor * TAXAS_CAMBIO[chave]
    return None

def entrada_float(mensagem):
    try:
        return float(input(mensagem))
    except ValueError:
        print("⚠️ Entrada inválida. Digite apenas números.")
        return None

def menu_temperatura():
    valor = entrada_float("Digite o valor da temperatura: ")
    if valor is None: return
    origem = input("Origem (C/F): ").upper()
    destino = input("Destino (C/F): ").upper()
    resultado = converter_temperatura(valor, origem, destino)
    print(f"✅ {valor}{origem} = {resultado:.2f}{destino}" if resultado else "⚠️ Conversão inválida.")

def menu_moeda():
    valor = entrada_float("Digite o valor em moeda: ")
    if valor is None: return
    origem = input("Moeda origem (USD, BRL, EUR): ").upper()
    destino = input("Moeda destino (USD, BRL, EUR): ").upper()
    resultado = converter_moeda(valor, origem, destino)
    print(f"✅ {valor} {origem} = {resultado:.2f} {destino}" if resultado else "⚠️ Conversão inválida ou não disponível.")

def menu():
    opcoes = [
        "\n=== CONVERSOR INTERATIVO ===",
        "1 - Temperatura 🌡️",
        "2 - Moeda 💱",
        "0 - Sair 🚪"
    ]

    while True:
        for item in opcoes: print(item)
        escolha = input("Escolha: ")

        if escolha == "1":
            menu_temperatura()
        elif escolha == "2":
            menu_moeda()
        elif escolha == "0":
            print("👋 Obrigado por usar o conversor!")
            break
        else:
            print("⚠️ Opção inválida.")

if __name__ == "__main__":
    menu()
