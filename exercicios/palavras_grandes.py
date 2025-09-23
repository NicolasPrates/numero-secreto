def palavras_grandes(texto):
    palavras_separadas = texto.split(' ')
    lista_de_palavras_grandes = []
    for palavra in palavras_separadas:
        if len(palavra) >= 10:
            lista_de_palavras_grandes.append(palavra)
    return lista_de_palavras_grandes

entrada = 'Um exemplo de texto grande com algumas palavras grandes paralelepipedo é uma delas, a outra é ortorrinolaringologista'

saida = palavras_grandes(entrada)
print(saida)