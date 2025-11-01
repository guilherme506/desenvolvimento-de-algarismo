class main:
    pass


print("Testando o projeto")

from cliente import cliente
from conta import conta

c1 = cliente("joão", "114444-2222")

print(c1)
print(c1.nome, "e", c1.telefone)
conta=conta(c1.get_nome(),1222)

conta.deposito(100)
conta.saque(50)
conta.extrato()