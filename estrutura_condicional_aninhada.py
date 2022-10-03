conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450
 
if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque relalizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o Saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu o tipo de conta, entre em contato com seu gerente")