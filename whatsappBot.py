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