def validar_cpf(numero_cpf):
    if not numero_cpf.isdigit():
        return('Entrada invalida, digite novamente com numeros apenas')
    elif len(numero_cpf) != 11:
        return('Entrada invalida, digite 11 numeros para um cpf valido')
    else:
        return('CPF valido')
    
    
input_cpf = input('Digite o CPF: ')
validacao_cpf = validar_cpf(input_cpf)
print(validacao_cpf)