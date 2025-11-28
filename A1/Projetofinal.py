# Sistema de verificação de idade para entrada em eventos
# Utiliza condicionais, repetição, listas e dicionários


#dicionario
eventos = [
    {"nome": "Festa apaga tudo", "idade_minima": 12},
    {"nome": "Balada jovem", "idade_minima": 16},
    {"nome": "Paradão", "idade_minima": 18},
    {"nome": "Cassino", "idade_minima": 21}
]
#listya
pessoas_registradas = []

print("=== Sistema de Verificação de Idade ===")

#While
while True:
    nome = input("\nDigite seu nome (ou 'sair' para encerrar): ").strip()
    if nome.lower() == "sair":
        break

    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida! Digite apenas números.")
        continue

    pessoa = {"nome": nome, "idade": idade}
    pessoas_registradas.append(pessoa)

    print("\nEventos disponíveis para você:")
    liberados = False

    # Verifica quais eventos a pessoa pode entrar
    #for
    for evento in eventos:
        if idade >= evento["idade_minima"]:
            print(f"✔ {evento['nome']} (idade mínima: {evento['idade_minima']})")
            liberados = True

    if not liberados:
        print("Infelizmente você não tem idade para nenhum evento.")

print("\n=== Relatório Final ===")
if len(pessoas_registradas) == 0:
    print("Nenhuma pessoa registrada.")
else:
    for pessoa in pessoas_registradas:
        print(f"- {pessoa['nome']}, {pessoa['idade']} anos")

print("Programa encerrado.")
