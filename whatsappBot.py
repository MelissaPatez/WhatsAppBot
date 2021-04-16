# Importar as libs
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#Navegar até whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(12)

#Contatos/Grupos e a Menssagem 
contato = ['Contato']
mensagens = [ 'menssagem1', 'mensssagem2', 'messagem3']

#Buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)

#Campo de pesquisa 'copyable-text selectable-text'
#Campo de texto 'copyable-text selectable-text'
def enviar_mensagem(mensagens):
    for mensagem in mensagens:
        for i in range(0, 1):
            campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
            campo_mensagem[1].click()
            campo_mensagem[1].send_keys(mensagem)
            campo_mensagem[1].send_keys(Keys.ENTER)

if __name__ == '__main__':
    buscar_contato(contato)
    enviar_mensagem(mensagens)