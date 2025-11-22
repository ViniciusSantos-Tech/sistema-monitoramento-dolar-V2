#𝙁𝙚𝙞𝙩𝙤 𝙥𝙤𝙧 𝙑𝙞𝙣𝙞𝙘𝙞𝙪𝙨 𝙎𝙖𝙣𝙩𝙤𝙨-𝙏𝙚𝙘𝙝
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import customtkinter as ctk
from time import sleep

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
    
def abrir_tela2():
    Tela2 = ctk.CTk()
    Tela2.geometry("500x500")
    Tela2.title("Cotações de Moedas")
    
    Valores()
    
    titulo = ctk.CTkLabel(Tela2, text="COTAÇÕES DE MOEDAS", font=("Arial", 20, "bold"))
    titulo.pack(pady=10)
    frame_tabela = ctk.CTkFrame(Tela2)
    frame_tabela.pack(pady=20, padx=20, fill="both", expand=True)
    cabecalho_moeda = ctk.CTkLabel(frame_tabela, text="MOEDA", font=("Arial", 14, "bold"))
    cabecalho_moeda.grid(row=0, column=0, padx=10, pady=5)
    
    cabecalho_valor = ctk.CTkLabel(frame_tabela, text="VALOR", font=("Arial", 14, "bold"))
    cabecalho_valor.grid(row=0, column=1, padx=10, pady=5)
    moedas = ['USD', 'EUR', 'JPY', 'AUD', 'GBP', 'CHF', 'CAD', 'TRY', 'CNY']
    
    for i, (moeda, valor) in enumerate(zip(moedas, Moedas), 1):
        label_moeda = ctk.CTkLabel(frame_tabela, text=moeda, font=("Arial", 12))
        label_moeda.grid(row=i, column=0, padx=10, pady=3)
        label_valor = ctk.CTkLabel(frame_tabela, text=valor, font=("Arial", 12))
        label_valor.grid(row=i, column=1, padx=10, pady=3)
    
    Login.destroy()
    Tela2.mainloop()
def Validar_login():
    usuario = Entrada.get()
    senha = Entrada2.get()
    if usuario == 'Vinicius' and senha == '12345':
         Label3.configure(text= 'Login feito com sucesso!', text_color= 'green')
         sleep(2)
         abrir_tela2()
    else:
         Label3.configure(text= 'Senha ou Usuario estao incorretos!', text_color= 'red')

Login = ctk.CTk()
Login.geometry("300x300")
Login.resizable(False, False)
Label = ctk.CTkLabel(Login, text='LOGIN')
Label.pack(pady=20, padx=1)
Entrada = ctk.CTkEntry(Login, placeholder_text='Username')
Entrada.pack()

Label2 = ctk.CTkLabel(Login, text='Senha')
Label2.pack()
Entrada2 = ctk.CTkEntry(Login, placeholder_text='Pasword')
Entrada2.pack(pady=10)

Botao = ctk.CTkButton(Login, text='Entrar', command=Validar_login)
Botao.pack()

Label3 = ctk.CTkLabel(Login, text=(" "))
Label3.pack(padx=10)
tela_aberta = None
Login.mainloop()
