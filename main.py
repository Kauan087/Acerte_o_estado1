import random
from rich import *
from rich.table import Table
import os
import platform
import pygame

def tocar_som(som):
    pygame.mixer.init()
    pygame.mixer.music.load(f"sons/{som}.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def limpar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


estados_brasil = {
    "Acre": "AC",
    "Alagoas": "AL",
    "Amapá": "AP",
    "Amazonas": "AM",
    "Bahia": "BA",
    "Ceará": "CE",
    "Distrito Federal": "DF",
    "Espírito Santo": "ES",
    "Goiás": "GO",
    "Maranhão": "MA",
    "Mato Grosso": "MT",
    "Mato Grosso do Sul": "MS",
    "Minas Gerais": "MG",
    "Pará": "PA",
    "Paraíba": "PB",
    "Paraná": "PR",
    "Pernambuco": "PE",
    "Piauí": "PI",
    "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN",
    "Rio Grande do Sul": "RS",
    "Rondônia": "RO",
    "Roraima": "RR",
    "Santa Catarina": "SC",
    "São Paulo": "SP",
    "Sergipe": "SE",
    "Tocantins": "TO"
}

while True:
    print('-=' * 30)
    print('                     [bold]Adivinhe o Estado[/]')
    print('-=' * 30)
    print('SELECIONE UMA OPÇÃO:')
    print("""
    [1] Começar jogo. 
    [2] ver tabelas dos estados.  
    [3] Sair do jogo.
    """)

    while True:
        try:
            menu = int(input('Selecione uma opção: '))
            if 1 <= menu <= 3:
                break  
            else:
                print('[red]Opção inválida![red]')  
        except ValueError:
            print('[red]Opção inválida![red]')  
    print('-=' * 20)

    if menu == 1:
         while True:
            cont = 0
            acertos = 0
            limpar_terminal()
            while cont < 5:
                estados = list(estados_brasil.items())
                estado_sorteado, sigla_sorteada = random.choice(estados)
                print('-'*16,f'[bold]{estado_sorteado}[/]','-'*16)
                print('-=' * 20)
                pergunta = str(input('Qual sigla desse estado? ')).upper()
                cont += 1
                if pergunta == sigla_sorteada:
                    print('[bold][green]Você acertou[green][/]!')
                    acertos += 1
                    tocar_som("acerto")

                else:
                    print('[bold][red]você errou[red][/]!')
                    tocar_som('erro')
            print(f'Você Acertou [green]{acertos}/5[/]')
            tocar_som('conclusao')
            print('deseja continuar?')
            print('[1] Sim.')
            print('[2] Não.')
            while True:
                try:
                    pergunta01 = int(input('Selecione uma opção: '))
                    if pergunta01 == 1:
                        limpar_terminal()
                        break  
                    elif pergunta01 == 2:
                        print('encerrando o jogo... ')
                        exit()   
                    else:
                        print('[red]Opção inválida![red]')  
                except ValueError:
                    print('[red]Opção inválida![red]')  
            print('-=' * 20)
                        
    if menu == 2:

        limpar_terminal()
        tabela = Table(title='[bold]Estados Brasileiros[/]')
        tabela.add_column('[bold]Estado[/]')
        tabela.add_column('[bold]sigla[/]')
        for estado, sigla in estados_brasil.items():
            tabela.add_row(f'{estado}', f'{sigla}')
        print(tabela)
        print('-=' * 20)
        print('        [bold]Selecione uma opção:[/]')
        print('-=' * 20)
        print('[1] Sair do jogo.')
        print('[2] Voltar para menu.')
      
        while True:
            try:
                pergunta02 = int(input('Selecione uma opção: '))
                if 1 <= pergunta02 <= 2:
                    limpar_terminal()
                    break  
                else:
                    print('[red]Opção inválida![red]')  
            except ValueError:
                print('[red]Opção inválida![red]')  
            print('-=' * 20)

        if pergunta02 == 1:
            print('Volte sempre!')
            break
        else:
            pass

    if menu == 3:
        print('Obrigado por jogar!')
        break
    
