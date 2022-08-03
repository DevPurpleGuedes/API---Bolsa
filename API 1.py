import requests
import json
import PySimpleGUI as sg

def window():
    
    tela_principal = sg.Window('Cotação do Dolar', layout= [
        [sg.Text ('Olá ! Gostaria de saber de a cotação de qual moeda hoje ?')],
        [sg.Checkbox('Dolar', k='Dolar'), sg.Checkbox('Euro', k='Euro'), sg.Checkbox('BitCoin', k='Bitcoin')],
        [sg.Button('Enviar'), sg.Button('Sair')]
    ])
    
    while True:
        
        evento, values  = tela_principal.read()
        
        if evento == sg.WIN_CLOSED or evento == 'Sair':
            break
        if evento == 'Enviar' and values['Dolar'] == True: 
            print(cotacao_dolar())
        if evento == 'Enviar' and values['Euro'] == True: 
            print(cotacao_euro())
        if evento == 'Enviar' and values['Bitcoin'] == True: 
            print(cotacao_bitcoin())
        
    tela_principal.close()
    

def cotacao_dolar():
    
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = cotacao.json()
    valor = cotacao ['USDBRL'] ['bid'] 
    return valor
    
def cotacao_euro():
        
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = cotacao.json()
    valor = cotacao ['EURBRL'] ['bid'] 
    return valor

def cotacao_bitcoin():
    
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = cotacao.json()
    valor = cotacao ['BTCBRL'] ['bid'] 
    return valor

window()