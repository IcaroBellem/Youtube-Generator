# YouTube Playlist Report Generator

Este projeto automatiza a geração de relatórios baseados nos títulos de vídeos de uma playlist específica do YouTube, usando a API do YouTube e a IA generativa do Google (Gemini). Os relatórios são gerados com base em diferentes perspectivas gerenciais, como DevOps, gestão de projetos e gestão de repositórios, e são salvos em um arquivo de texto.

## Requisitos

- Python 3.7 ou superior
- Windows Subsystem for Linux (WSL)
- Conta Google Cloud com acesso à API do YouTube e ao Google Gemini

## Configuração do Ambiente

### 1. Configurando o WSL

Se você ainda não tem o WSL instalado, siga os passos abaixo:

1. Abra o PowerShell como Administrador e execute o comando abaixo para instalar o WSL:
   ```bash
   wsl --install
Após a instalação, reinicie o seu computador.

Quando o sistema reiniciar, abra o WSL e configure o Ubuntu (ou a distribuição Linux de sua escolha).

Atualize os pacotes do WSL:
```bash
sudo apt update && sudo apt upgrade -y
```


2. Instalando o Python no WSL
   
Instale o Python 3 no WSL:
```bash
sudo apt install python3 python3-pip
```
Verifique a instalação do Python:
```bash
python3 --version
pip3 --version
```
3. Instalando e Configurando o Ambiente Virtual
   
Crie um ambiente virtual chamado myvenv:
```bash
python3 -m venv myvenv
```
Ative o ambiente virtual:

No Windows (WSL):
```bash
source myvenv/bin/activate
```
No Linux/Mac:
```bash
source myvenv/bin/activate
```
Instale as dependências do projeto dentro do ambiente virtual:
```bash
pip install -r requirements.txt
```
Se o arquivo requirements.txt não estiver presente, crie um com o seguinte conteúdo:
```bash
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
google-generativeai
python-dotenv
```
4. Configurando o Projeto
Clone este repositório no WSL ou crie um novo diretório para o projeto:
```bash
git clone <URL-do-repositorio>
cd <nome-do-diretorio>
```
Crie um arquivo .env na raiz do projeto e adicione as suas chaves de API:
```bash
touch .env
```
O arquivo .env deve conter:
```bash
GOOGLE_API_KEY=your_google_gemini_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```
5. Excluindo Arquivos Binários do Controle de Versão
Certifique-se de que arquivos binários, como o diretório myvenv/, não estejam sendo versionados pelo Git. Adicione o diretório do ambiente virtual ao .gitignore:

Abra ou crie um arquivo .gitignore na raiz do seu repositório.

Adicione as seguintes linhas:
```bash
myvenv/
*.pyc
__pycache__/
```
6. Executando o Projeto
Execute o script principal:
```bash
python your_script_name.py
```
O script irá gerar relatórios baseados nos títulos dos vídeos da playlist especificada e salvá-los em um arquivo chamado devops_project_repo_reports.txt.

Estrutura do Projeto
```bash
├── your_script_name.py      # Script principal do projeto
├── .env                     # Arquivo de variáveis de ambiente
├── requirements.txt         # Arquivo com as dependências do projeto
├── myvenv/                  # Ambiente virtual (não versionado no Git)
└── devops_project_repo_reports.txt  # Arquivo gerado com os relatórios (após execução)
```
Observações

Certifique-se de que as chaves de API do Google estejam ativas e com as permissões necessárias para acessar a API do YouTube e o serviço Gemini.
O tempo de execução do script pode variar dependendo do número de vídeos na playlist e da complexidade dos prompts enviados ao modelo de IA.
