import os

from aluno import Aluno
from escola import Escola

def clear():
    os.system('clear')

def print_header(message):
    clear()
    print(f'-------------- {message} ---------------------')

def pressione_para_continuar():
    print('')
    input('Pressione qualquer tecla para continuar...')

def imprimir_menu():
    clear()
    print('Bem vindo ao console da escola UNIFACISA')
    print('Por favor digite o numero da operação')
    print('1 - Adicionar Aluno')
    print('2 - Visualizar os aluno')

    print('')

def visualizar_alunos(escola):
    print_header('Visualizar Alunos')
    escola.visualizar_alunos()
    pressione_para_continuar()

def adicionar_aluno(escola):
    print_header('Adicionar Aluno')
    nome = input('Digite o nome do aluno: ')
    escola.add_aluno(nome)
    pressione_para_continuar()

if __name__ == "__main__":
    escola = Escola('UNIFACISA')
    ativo = True
    while ativo:
        imprimir_menu()
        opcao = input('Opção ')
        opcoes = {
            1: adicionar_aluno,
            2: visualizar_alunos
        }
        opcoes[int(opcao)](escola)
        

    
    