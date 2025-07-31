def caixa():
    saldo=int(input("digite o saldo bancario"))
    saque=int(input("digite o valor do saque"))
    if saldo>=saque:
        saldo-=saque
        print("voce realizou um saque com sucesso.")
    else:
       print("vove nao possui saldo suficiente para realizar essa operacao.")
       print("voce nao possui saldo suficiente")
#caixa()
def deposito():
    saldo=int(input("digite o saldo bancario"))
    pix=int(input("20"))
    saldo+=pix
    print("seu sado e:",saldo) 
    deposito()

def porcentagem():
    valor_parte=float(input("insirao valor parte:"))
    porcentagem=float(input("insira o vfalor da porcentagem:"))
    valor_total=valor_parte*(porcentagem/100)
    print(porcentagem=100)
    


















