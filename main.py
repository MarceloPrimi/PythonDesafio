from Modulos.Web import Automacao
from Modulos.consultaAPI import consultar_api
from Modulos.applegado import buscar_dados_legado


def main():
    try:
        automacao = Automacao()
        automacao.executar_para_varios_ids()
    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()
