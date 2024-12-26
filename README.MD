# Employee Data Migration Project

Este projeto tem como objetivo migrar dados de funcionários de um sistema legado e de uma API para um novo sistema de gerenciamento de recursos humanos, automatizando o preenchimento de formulários na interface web.

## Estrutura do Projeto

```
project/
├── main.py
├── .env
├── README.md
├── Modulos/
│   ├── web.py
│   ├── consultaAPI.py
│   ├── applegado.py
```

### Descrição dos Arquivos

- **main.py**: Arquivo principal que orquestra a execução do projeto.
- **.env**: Arquivo para armazenar credenciais sensíveis, como email e senha.
- **Modulos/web.py**: Contém a lógica principal para acessar o site, realizar login, coletar IDs, consultar a API e preencher o formulário.
- **Modulos/consultaAPI.py**: Realiza a consulta na API para obter informações adicionais dos funcionários.
- **Modulos/applegado.py**: Interage com o aplicativo legado para buscar dados complementares dos funcionários.

## Pré-requisitos

1. **Python**: Certifique-se de ter o Python 3.10+ instalado.
2. **Bibliotecas**:
   - Selenium: Para automação de navegadores web. 
   - Pywinauto: Para interação e automação de aplicativos desktop, especificamente o Applegado.
   - dotenv: Para gerenciar variáveis de ambiente, como credenciais do login no site.
   - Pandas: Para manipulação de dados estruturados em forma de tabelas (DataFrames), combinando dados da API e do aplicativo legado.
   - keyboard: Para detectar e aguardar a tecla "ESC" como comando para encerrar o navegador após a execução.
   - time: Para pausas entre interações e controle de tempo.
   - os: Para manipulação de caminhos e integração com o sistema operacional.

3. **ChromeDriver**:
   Certifique-se de que o ChromeDriver está instalado e compatível com a versão do Google Chrome.

## Configuração

1. Crie um arquivo `.env` na raiz do projeto com o seguinte formato:
   ```
   LOGIN_EMAIL=seu_email
   LOGIN_PASSWORD=sua_senha
   ```

2. Organize a estrutura do projeto como descrito acima.

## Funcionalidades

### 1. **Login Automático**
   - Acesse o site do desafio.
   - Aceite cookies.
   - Realize login utilizando credenciais fornecidas no `.env`.

### 2. **Coleta de IDs**
   - Coleta IDs de funcionários diretamente do site.

### 3. **Consulta à API**
   - Consulta informações adicionais, como telefone e data de início, utilizando a API fornecida.

### 4. **Interação com o Sistema Legado**
   - Busca informações complementares no aplicativo legado, como nome, email, cargo, etc. (Necessario ajustar o caminho do arquivo na maquina local em app_path)

### 5. **Preenchimento de Formulário**
   - Preenche o formulário do novo sistema de gerenciamento de recursos humanos com os dados combinados (API + sistema legado).

### 6. **Processamento de Múltiplos IDs**
   - Processa até 10 IDs por vez, mantendo o navegador aberto ao final.

## Como Executar

1. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```

2. O script realizará o login, coletará IDs, consultará dados na API e no sistema legado e preencherá o formulário automaticamente.

3. Após processar 10 IDs, o navegador será mantido aberto até que a tecla `ESC` seja pressionada.

## Observação
   ```
   A velocidade que o bot é executado vai de acordo com a "potencia" da sua maquina e a velocidade da internet
   ```

## Este projeto foi desenvolvido por:
`Marcelo Primi Reballo`


