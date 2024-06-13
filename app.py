from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Configuração do WebDriver do Chrome
    driver = webdriver.Chrome()

    try:
        # Abre o Instagram
        driver.get('https://www.instagram.com/accounts/login/')

        # Aguarda a página carregar
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )

        # Encontra os campos de entrada e insere as credenciais
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submete o formulário
        password_field.send_keys(Keys.RETURN)

        # Aguarda o login completar
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/direct/inbox/')]"))
        )

        return "Login bem-sucedido!"

    finally:
        # Fecha o navegador
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
