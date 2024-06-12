from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

# Rota para lidar com o login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

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
        password_field = driver.find_element(By.NAME, 'password')

        username.send_keys(email)  # Insere o email
        password_field.send_keys(password)    # Insere a senha

        # Submete o formulário
        password_field.send_keys(Keys.RETURN)

        # Aguarda o login completar
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/direct/inbox/')]"))
        )

        print("Login bem-sucedido!")

        return jsonify({"message": "Login bem-sucedido!"}), 200

    except Exception as e:
        print("Erro durante o login:", e)
        return jsonify({"error": "Ocorreu um erro durante o login."}), 500

    finally:
        # Fecha o navegador
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
