class ContaBancaria():
    
    def __init__(self, titular, saldo, numero_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        
    def depositar(self, valor):
        
        if valor > 0:
            self.saldo += valor
            print('Depósito realizado com sucesso!')
        else:
            print('Erro: Digite um valor válido ( > 0)')
        
    def sacar(self, valor):
        
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente para realizar o saque')
    
    def transferir(self, valor, conta_destino):
        
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            
            print(f'{self.titular} transferiu R$ {valor:.2f} para {conta_destino.titular}')
        else:
            print('Saldo insuficiente para realizar a transferência')
            
    def mostrar_dados(self):
        print(f'Titular: {self.titular} \nConta: {self.numero_conta} \nSaldo: R$ {self.saldo:.2f}')
        
conta1 = ContaBancaria('Arthur', 1000, '001')
conta2 = ContaBancaria('Maria', 500, '002')

conta1.mostrar_dados()
print()
conta2.mostrar_dados()
print()
conta1.depositar(300)
conta1.mostrar_dados()
print()
conta1.sacar(200)
conta1.mostrar_dados()
print()
conta2.sacar(1000)
print()
print()
conta1.transferir(400, conta2)

print()
conta1.mostrar_dados()
print()
conta2.mostrar_dados()