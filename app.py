import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa','ativo':False},
                {'nome':'pizza suprema','categoria':'pizza','ativo':True},
                {'nome':'Cantina', 'categoria':'italiano','ativo':False}]

def exibir_nome_do_programa(): 
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. listar  restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizando_app():
    exibir_subtitulo ('finalizando app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes\n')
    nome_do_restaurante = input ('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'digite o nome da categoria do restaurante{nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso!!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes:\n')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)}| Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('ativar/desativar restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
       if nome_do_restaurante == restaurante['nome']:
          restaurante_encontrado = True
          restaurante['ativo'] = not restaurante['ativo']
          mensagem = f'O restaurante: {nome_do_restaurante} foi ativado com sucesso' \
            if restaurante['ativo'] else f'O restaurante: {nome_do_restaurante} foi desativado com sucesso'
          print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')      

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input ('Escolha uma opção: '))
        if opcao_escolhida ==  1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif  opcao_escolhida == 4:
            finalizando_app()    
        else:
            opcao_invalida()   
    except:
        opcao_invalida()

def main():
  os.system ('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
    main()