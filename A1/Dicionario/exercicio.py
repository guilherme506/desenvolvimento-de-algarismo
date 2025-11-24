produtos = {}

quantidade = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade):
    nome = input(f"Nome do produto {i+1}: ")
    preco = float(input(f"Preço do produto {i+1}: "))
    produtos[nome] = preco

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome} - R$ {preco:.2f}")
