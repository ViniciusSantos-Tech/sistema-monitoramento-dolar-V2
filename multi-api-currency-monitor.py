#Feito por Vinicius Santos-Tech
#Aprendendo APIs
def relatorio():
    
    print(f"Contaçao do AwesomeApi: {Contaçao1}")
    print(f"Contaçao do Banco do brasil: {Contaçao2}")
    print(f"Contaçao de um site é: {Contaçao3}")
    print("Proxim relatorio em 24hrs.")
    time.sleep(3600)

import requests
import time

def Contaçao():
    url1 = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    url2 = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1"
    url3 = "https://br.dolarapi.com/v1/cotacoes/usd"

    dado1 = requests.get(url1)
    dado2 = requests.get(url2)
    dado3 = requests.get(url3)

    dado1_json = dado1.json()
    dado2_json = dado2.json()
    dado3_json = dado3.json()

    Contaçao1 = float(dado1_json['USDBRL']['bid'])
    Contaçao2 = float(dado2_json[0]['valor'])
    Contaçao3 = float(dado3_json['compra'])


    Média_tudo = (Contaçao1 + Contaçao2 + Contaçao3) / 3
    print(f"A média de tudo é: {Média_tudo:.2f}")
    if Média_tudo <= 5.20:
        print("Alerta! O dolar caiu Demais! ")
    elif Média_tudo >= 5.80:
        print("Alerta! O dolar passou de 5.80 ")
    else:
        print("dolar na faixa normal")

    
    print(f"Contaçao do AwesomeApi: {Contaçao1:.2f}")
    print(f"Contaçao do Banco do brasil: {Contaçao2:.2f}")
    print(f"Contaçao de um site é: {Contaçao3:.2f}")
    print("Proximo relatorio em 24hrs.")


Rodar = True
while Rodar:
 
    Contaçao()
    time.sleep(3600)
