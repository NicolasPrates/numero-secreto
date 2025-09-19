import os

restaurantes = [
      {'nome':'praca', 'categoria':'Japonesa', 'ativo':False}, 
      {'nome':'massasEmolhos', 'categoria':'Italiana', 'ativo':True},
      {'nome':'mexidos', 'categoria':'Brasileira', 'ativo':False}             
]

def exibir_nome_do_programa():
      print("""
      
╭━━━┳━━━┳━━╮╭━━━┳━━━╮  ╭━━━┳━╮╭━┳━━━┳━━━┳━━━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭╮┃┃╭━╮┃╭━╮┃  ┃╭━━┻╮╰╯╭┫╭━╮┃╭━╮┃╭━━┫╭━╮┃╭━╮┃
┃╰━━┫┃╱┃┃╰╯╰┫┃╱┃┃╰━╯┃  ┃╰━━╮╰╮╭╯┃╰━╯┃╰━╯┃╰━━┫╰━━┫╰━━╮
╰━━╮┃╰━╯┃╭━╮┃┃╱┃┃╭╮╭╯  ┃╭━━╯╭╯╰╮┃╭━━┫╭╮╭┫╭━━┻━━╮┣━━╮┃
┃╰━╯┃╭━╮┃╰━╯┃╰━╯┃┃┃╰╮  ┃╰━━┳╯╭╮╰┫┃╱╱┃┃┃╰┫╰━━┫╰━╯┃╰━╯┃
╰━━━┻╯╱╰┻━━━┻━━━┻╯╰━╯  ╰━━━┻━╯╰━┻╯╱╱╰╯╰━┻━━━┻━━━┻━━━╯
      
      """)

def voltar_ao_menu_principal():
      '''Funcao de retorno ao menu principal'''
      input('\nDigite uma tecla para voltar ao menu principal ')
      main()
      
def exibir_subtitulo(texto):
      '''Funcao responsavel por exibir o subtitulo'''
      os.system('cls')
      linha ='*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def exibir_opcaoes():
      '''Função responsável por exibir as opções no menu principal'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar Estado do Restaurante')
      print('4. Fechar o Aplicativo')

def finalizar_app():
      '''Função responsável por finalizar o aplicativo'''
      exibir_subtitulo('Finalizando o App\n')
      
def opcao_invalida():
      '''Funcao que retoma o fluxo principal caso a pessoa escolha uma opção inválida no menu principal'''
      print('Opcao invalida\n')
      voltar_ao_menu_principal()
      
def cadastrar_novo_restaurante():
      '''Essa funcao é responsavel por cadastrar um novo restaurante'''
      exibir_subtitulo('cadastro de novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
      voltar_ao_menu_principal()
      
def alternar_estado_restaurante():
      '''Alterna o estado dos restaurantes entre ativado e desativado'''
      exibir_subtitulo('Alternando estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
      restaurante_encontrado = False
      
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado'
                  print(mensagem)
                  
      if not restaurante_encontrado:
            print('Restaurante não encontrado')
            
      voltar_ao_menu_principal()
      
      
def listar_restaurantes():
      exibir_subtitulo('Listando Restaurantes')
      print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
      for restaurante in restaurantes:
            categoria = restaurante['categoria']
            nome_restaurante = restaurante['nome']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
      voltar_ao_menu_principal()


def escolher_opcao():
      opcao_escolhida = input('Escolha uma opção: ')
      print(f'Você escolheua opção {opcao_escolhida}!')
      try:
            opcao_escolhida = int(opcao_escolhida) 

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()



      
def main():
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcaoes()
      escolher_opcao()

if __name__ == '__main__':
      main()