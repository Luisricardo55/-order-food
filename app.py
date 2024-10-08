import os

restaurantes = [ {'nome': 'Pizza', 'categoria': 'italiana', 'ativo': 'False'},
                 {'nome': 'sushi', 'categoria': 'japonesa', 'ativo': 'True'} ]        
                 

def exibir_nome_do_programa():
    print('''   
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
      
      ''')

def exibir_opcoes():
    '''exibi as opcoes'''
    print('1. Casdrastrar restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def voltar_para_o_menu():
     input('\nDigite uma tecla para voltar ao menu principal: ')
     main()

def exibir_subtitulo(texto):
    os.system('cls')
    cobertura = '-' * (len(texto))
    print(cobertura)
    print(texto)
    print(cobertura)
    print()

def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    voltar_para_o_menu()

def opcao_invalida():
     '''opcao invalida'''
     exibir_subtitulo('Opção invalida')
     voltar_para_o_menu()

def cadastrar_novo_restaurante():
     '''cadrastar novos restaurantes
     
     INPUTS:
     -categoria
     -nome_do_restaruante

     OUTPUTS:
     -adiciona um novo restaurante na lista de restaurantes 
     '''
     exibir_subtitulo('Cadastrar novos restaurantes')
     nome_do_restaurante = input('Digite o nome do restaurante: ')
     categoria = input('Digite a categoria do seu restaurante {nome_do_restaurante}:  ' )
     dados_do_restaurante = { 'nome' : nome_do_restaurante,
    'categoria' :categoria, 'ativo' :False }
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
     voltar_para_o_menu()

def listando_os_restaurantes():
    '''lista de restarantes
    
    INPUTS:
    -sem

    OUTPUTS:
    -sem
    '''
    exibir_subtitulo('Listando os restaurantes')

    #quando for assim utilize "" e no ultimo''
    print(f'{"Restaurantes:".ljust(15)} | {"Categoria:".ljust(15)} | Status:')
    for restaurante in restaurantes:
    
        nome_restaurante = restaurante ['nome']
        categ_rest = restaurante ['categoria']
        ativo_rest = 'Ativado' if restaurante ['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(15)} '  ' | '  f'{categ_rest.ljust(15)} '  ' | '  f'{ativo_rest.ljust(15)}')
     #print(f'Restaurantes listados: {restaurantes}') tambem pega
    voltar_para_o_menu()


def alternar_estado_restaurante():
    '''ativo/desativo
    
    INPUTS:
    -nome_restaurante

    OUTPUTS:
    -ativa ou desativa o restaunte em lista dos restaurantes
    '''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
     print('O restaurante não foi encontrado.')
    voltar_para_o_menu()


def escolher_funcao():

    while True:  # Loop para pedir a entrada até que seja válida
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))
            if 1 <= opcao_escolhida <= 4:  # Verifica se a opção está no intervalo válido
                break  # Sai do loop se a opção for válida
            else:
                opcao_invalida()  # Chama a função opcao_invalida() se a opção for inválida
        except ValueError:
            opcao_invalida()  # Chama a função opcao_invalida() se a entrada for inválida

    # Resto do código para executar a função escolhida
    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listando_os_restaurantes()
    elif opcao_escolhida == 3:
        alternar_estado_restaurante()
    # ... e assim por diante

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_funcao()
    

if __name__=='__main__':
 main()
