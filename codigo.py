"""
Projeto de automação de cadastro de produtos.

O script lê um arquivo CSV com produtos e realiza o cadastro automático
em um sistema web utilizando PyAutoGUI.
"""

# bibliotecas = pacote de código 
# pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo a passo do meu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: Fazer login
# clicar no campo de email
pyautogui.click(x=692, y=404) # para clicar no campo de email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("automacao-cadastro-produtos-python\produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    # Código
    pyautogui.click(x=528, y=282) # para clicar no campo código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # Preço 
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    # voltar para o início da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos