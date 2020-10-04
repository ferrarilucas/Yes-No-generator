import random
import PySimpleGUI as sg

answers = [
    'Sim',
    'Não',
    'Talvez',
    'Com certeza',
    'Nem pensar',
    'Vai que é sucesso',
    'Quem sabe um dia',
    'Hoje não',
    'Não sei',
    'Vai, mas vai com calma',
    'Acho que sim',
    'Acho que não',
    'Pergunta mais tarde',
    'Pergunta outra coisa',
    'Não vou responder isso',
    'Tu sabe o que tem que fazer'
]

sg.theme('DarkAmber')

layout_main = [
    [sg.Text('Digite uma pergunta de sim ou não')],
    [sg.InputText()],
    [sg.Button("Ok"), sg.Button("Cancelar")]
]


mainpage = sg.Window('Sim ou não gerador ', layout_main,
                     element_justification='center')
while True:
    event, value = mainpage.read()
    if event == 'Ok':
        sg.popup(random.choice(answers), title='Resposta')
    if event in (sg.WIN_CLOSED, 'Cancelar'):
        mainpage.close()
        break

# mainpage.close()
