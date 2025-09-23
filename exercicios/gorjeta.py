def gorjeta():
    valor_conta = float(input('Digite o valor da conta: '))
    porcentagem_gorjeta = float(input('Digite a porcentagem da gorjeta: '))/100.00
    return valor_conta*porcentagem_gorjeta, valor_conta + valor_conta*porcentagem_gorjeta

valor_gorjeta = gorjeta()
print('Valor da gorjeta: ', valor_gorjeta[0])
print('Valor total da conta: ', valor_gorjeta[1])