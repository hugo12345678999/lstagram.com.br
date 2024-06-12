from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o WebDriver do Chrome
driver = webdriver.Chrome()

try:
    # Abre o Instagram
    driver.get('https://www.instagram.com/accounts/login/')

    # Aguarda a página carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )

    # Encontra os campos de entrada e insere as credenciais
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')

    username.send_keys('mahiiu66')  # Substitua 'seu_usuario' pelo seu nome de usuário
    password.send_keys('Maria*280810*')    # Substitua 'sua_senha' pela sua senha

    # Submete o formulário
    password.send_keys(Keys.RETURN)

    # Aguarda o login completar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/direct/inbox/')]"))
    )

    print("Login bem-sucedido!")

finally:
    # Fecha o navegador
    driver.quit()
