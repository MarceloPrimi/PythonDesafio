from pywinauto import Application
import pandas as pd
import time


def buscar_dados_legado(employee_id):
    try:
        # Caminho para o aplicativo legado
        app_path = r"C:\Users\Marcelo\Documents\Legado\EmployeeList.exe"

        # Inicia o aplicativo
        try:
            app = Application().start(app_path)
            window = app.window(title="Employee Database") 
        except Exception as e:
            print(f"Erro ao iniciar o aplicativo ou localizar a janela principal: {e}")
            return None

        # Localizar o campo de ID e inserir o texto
        try:
            id_field = window.child_window(auto_id="txtEmpId")  
            id_field.set_text(employee_id)
            time.sleep(0.5)
        except Exception as e:
            print(f"Erro ao localizar o campo de ID ou inserir o texto: {e}")
            return None

        # Clicar no botão de pesquisa
        try:
            search_button = window.child_window(auto_id="btnSearch")  
            search_button.click_input()
            window.wait('ready', timeout=10)  # Aguarda os dados serem carregados
        except Exception as e:
            print(f"Erro ao localizar ou clicar no botão de pesquisa: {e}")
            return None

        # Coletar dados dos campos
        try:
            campos = {
                "First Name": "txtFirstName",
                "Last Name": "txtLastName",
                "Email Address": "txtEmailId",
                "City": "txtCity",
                "State": "txtState",
                "Zip": "txtZip",
                "Job Title": "txtJobTitle",
                "Department": "txtDepartment",
                "Manager": "txtManager"
            }

            dados = {}
            for campo, identificador in campos.items():
                try:
                    elemento = window.child_window(auto_id=identificador)
                    dados[campo] = elemento.window_text()
                except Exception as e:
                    print(f"Erro ao coletar o campo '{campo}': {e}")
                    dados[campo] = None  # Define como None se houver falha na coleta

        except Exception as e:
            print(f"Erro ao coletar os dados dos campos: {e}")
            return None

        # Converter os dados em um DataFrame do Pandas
        try:
            df = pd.DataFrame([dados])
            print(f"Dados coletados do aplicativo legado:\n{df}")
        except Exception as e:
            print(f"Erro ao converter os dados para DataFrame: {e}")
            return None

        # Fechar o aplicativo
        try:
            app.kill()
        except Exception as e:
            print(f"Erro ao fechar o aplicativo: {e}")

        return df
    except Exception as e:
        print(f"Erro inesperado no processo: {e}")
        return None
