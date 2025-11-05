from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

from time import sleep
Moedas = []
Rodar = True

print("BEM VINDO!")
def Menu():
     print("----MENU----")
     print("1- Para ver contaçao Das 8 Principais moedas ")
     print("2- Para Sair")
     Resposta = input("Digite aqui sua opçao: ")
     if Resposta == "1":
          Valores()
     elif Resposta == "2":
        print("Encerrado")

def Valores():
    try:
          service = Service(ChromeDriverManager().install())
          driver = webdriver.Chrome(service=service)
          Site = driver.get("https://investidor10.com.br/moedas/")
          sleep(2)
          USD = driver.find_element(By.CSS_SELECTOR, ".points").text
          Moedas.append(USD)
          EUR = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[2]/a/div[2]/p[2]/strong').text
          Moedas.append(EUR)
          JPY = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[22]/a/div[2]/p[2]/strong').text
          Moedas.append(JPY)
          AUD = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[8]/a/div[2]/p[2]/strong').text
          Moedas.append(AUD)
          GBP = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[4]/a/div[2]/p[2]/strong').text
          Moedas.append(GBP)
          CHF = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[5]/a/div[2]/p[2]/strong').text
          Moedas.append(CHF)
          CAD = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[7]/a/div[2]/p[2]/strong').text
          Moedas.append(CAD)
          TRY = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[19]/a/div[2]/p[2]/strong').text
          Moedas.append(TRY)
          CNY = driver.find_element(By.XPATH, '//*[@id="indices-grid"]/div[13]/a/div[2]/p[2]/strong').text
          Moedas.append(CNY)
     
          driver.quit()
    except:
         print("Erro! Verifique sua internet.")
    tb = {
         'MOEDA': ['USD', 'EUR', 'JPY', 'AUD', 'GBP', 'CHF', 'CAD', 'TRY', 'CNY'],
         'VALOR': Moedas
    }
    Tabela = pd.DataFrame(tb)
    print("----------TABELA----------")
    print(Tabela)
    print("--------------------------")
    Tabela.to_excel('Moedas.xlsx')
    print("Tabela salva com sucesso!")
    MAIOR = max(Moedas)
    MENOR = min(Moedas)
    print(f"Maior valor: {MAIOR}")
    print(f"Menor valor: {MENOR}")
    
Menu()
