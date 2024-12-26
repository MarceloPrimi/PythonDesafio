import requests

def consultar_api(employee_id):
    api_url = "https://botgames-employee-data-migration-vwsrh7tyda-uc.a.run.app/employees?id="
    url = f"{api_url}{employee_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        data = response.json()
        print(f"Dados retornados pela API: {data}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
        return None
