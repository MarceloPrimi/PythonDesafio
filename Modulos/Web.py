from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from Modulos.consultaAPI import consultar_api
from Modulos.applegado import buscar_dados_legado
import os
import time
import keyboard

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Automacao:
    def __init__(self):
        self.url = "https://pathfinder.automationanywhere.com/challenges/automationanywherelabs-employeedatamigration.html"
        self.email = os.getenv("LOGIN_EMAIL")
        self.password = os.getenv("LOGIN_PASSWORD")
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)

    def abrir_navegador(self):
        self.driver.get(self.url)
        time.sleep(5)

    def aceitar_cookies(self):
        try:
            cookie_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            cookie_button.click()
            time.sleep(2)
        except Exception as e:
            print("Erro ao aceitar cookies:", e)

    def community_login(self):
        try:
            login_button = self.driver.find_element(By.ID, "button_modal-login-btn__iPh6x")
            login_button.click()
            time.sleep(5)
        except Exception as e:
            print("Erro ao abrir o modal de login:", e)

    def realizar_login(self):
        try:
            email_field = self.driver.find_element(By.XPATH, "//*[@id='43:2;a']")
            email_field.send_keys(self.email)
            email_field.send_keys(Keys.RETURN)
            time.sleep(3)

            password_field = self.driver.find_element(By.XPATH, "//*[@id='10:146;a']")
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.RETURN)
            time.sleep(5)
        except Exception as e:
            print("Erro ao realizar login:", e)

    def coletar_id(self):
        try:
            employee_id = self.driver.execute_script("return document.getElementById('employeeID').value;")
            print(f"ID coletado: {employee_id}")
            return employee_id
        except Exception as e:
            print("Erro ao coletar o ID:", e)
            return None

    def preencher_formulario(self, dados_combinados):
        try:
            self.driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys(dados_combinados["First Name"])
            self.driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys(dados_combinados["Last Name"])
            self.driver.find_element(By.XPATH, "//*[@id='phone']").send_keys(dados_combinados["phoneNumber"])
            self.driver.find_element(By.XPATH, "//*[@id='email']").send_keys(dados_combinados["Email Address"])
            self.driver.find_element(By.XPATH, "//*[@id='startDate']").send_keys(dados_combinados["startDate"])
            self.driver.find_element(By.XPATH, "//*[@id='city']").send_keys(dados_combinados["City"])
            self.driver.find_element(By.XPATH, "//*[@id='state']").send_keys(dados_combinados["State"])
            self.driver.find_element(By.XPATH, "//*[@id='zip']").send_keys(dados_combinados["Zip"])
            self.driver.find_element(By.XPATH, "//*[@id='title']").send_keys(dados_combinados["Job Title"])
            self.driver.find_element(By.XPATH, "//*[@id='department']").send_keys(dados_combinados["Department"])
            self.driver.find_element(By.XPATH, "//*[@id='manager']").send_keys(dados_combinados["Manager"])
            self.driver.find_element(By.XPATH, "//*[@id='submitButton']").click()
            
            print("Formulário submetido com sucesso!")
        except Exception as e:
            print(f"Erro ao preencher ou submeter o formulário: {e}")

    def executar_para_varios_ids(self):
        self.abrir_navegador()
        self.aceitar_cookies()
        self.community_login()
        self.realizar_login()

        id_count = 0
        while id_count < 10:
            employee_id = self.coletar_id()
            if not employee_id:
                print("Erro ao coletar o ID ou nenhum ID restante. Finalizando.")
                break

            print(f"Processando ID {id_count + 1}: {employee_id}")
            dados_api = consultar_api(employee_id)

            if dados_api:
                dados_legado = buscar_dados_legado(employee_id)
                if dados_legado is not None:
                    dados_combinados = {**dados_legado.to_dict('records')[0], **dados_api}
                    self.preencher_formulario(dados_combinados)
                else:
                    print(f"Erro ao coletar dados do aplicativo legado para ID: {employee_id}")
            else:
                print(f"Erro ao consultar a API para ID: {employee_id}")

            id_count += 1
            print(f"ID {employee_id} processado com sucesso. Total processado: {id_count}.")

        print("Limite de 10 IDs processado. Pressione ESC para fechar o navegador.")
        try:
            while True:
                if keyboard.is_pressed('esc'):
                    break
        except Exception as e:
            print("Erro ao aguardar comando de saída:", e)

def main():
    automacao = Automacao()
    try:
        automacao.executar_para_varios_ids()
    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()
