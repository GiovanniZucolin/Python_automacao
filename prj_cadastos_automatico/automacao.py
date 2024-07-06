# Importando biblioteca de automatização
import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# Pausa entre os comandos
pyautogui.PAUSE = 0.5

# Entrar no navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Pausa de 2 segundos
time.sleep(2)

# Fazer login
pyautogui.click(x=725, y=369)
pyautogui.write("Pingu.Luiz@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhablabla")
pyautogui.press("tab")
pyautogui.press("enter")
# Pausa de 2 segundos
time.sleep(2)

# Importar base de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Cadastrar produtos
for linha in tabela.index:
    pyautogui.click(x=574, y=254)
    # pegar da tabela o valor do campo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

    # para  interromper a execução do programa, basta mover manualmente o mouse para o
    # canto superior esquerdo da tela.