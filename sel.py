from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Crie um objeto webdriver.Remote para se conectar ao servidor remoto do Selenium
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=webdriver.DesiredCapabilities.CHROME)

# Abra o Google e pesquise por "python"
driver.get('https://www.infomoney.com.br/ultimas-noticias/')
print("conectado")

# Clique no botão "carregar mais" três vezes
for i in range(3):

    try:
        load_more_button = driver.find_element(by=By.XPATH, value="//button[contains(text(),'Carregar mais')]")
        print(load_more_button)
        load_more_button.click()
        time.sleep(2)  # aguarde 2 segundos para a página carregar
        print("click")
    except Exception as error:
        print(str(error))
        print("Não foi possível encontrar o botão 'carregar mais' na página.")
        break

# Feche o driver do Selenium
driver.quit()

