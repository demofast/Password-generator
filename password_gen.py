import random
import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        # Definir o tema da interface gráfica
        sg.theme('DarkAmber')

        # Definir o layout da janela
        layout = [
            [sg.Text('Site/Software', size=(15, 1)), sg.Input(key='site', size=(35, 1))],
            [sg.Text('Email/Usuário', size=(15, 1)), sg.Input(key='usuário', size=(35, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(8, 31)), key='total_chars', default_value=8, size=(3, 1))],
            [sg.Output(size=(50, 5))],
            [sg.Button('Gerar Senha'), sg.Button('Salvar Senha')]
        ]

        # Criar a janela com o layout definido
        self.janela = sg.Window('Gerador de Senhas', layout)

    def start(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores['total_chars'])
                print(nova_senha)
            if evento == 'Salvar Senha':
                nova_senha = self.gerar_senha(valores['total_chars'])
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, total_chars):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()-_=+[{]}\\|;:\'",<.>/?'
        chars = random.choices(char_list, k=int(total_chars))
        nova_senha = ''.join(chars)
        return nova_senha

    def salvar_senha(self, nova_senha, valores):
        with open('password.txt', 'a') as arquivo:
            arquivo.write(f'site: {valores["site"]}, usuário: {valores["usuário"]}, senha: {nova_senha}\n')
        print('Senha salva com sucesso!')

gen = PassGen()
gen.start()
