# Aplicação de Otimização de Rotas

Este projeto é uma aplicação FastAPI que calcula a rota mais curta entre cidades utilizando a API do Google Maps. 
Ele gera uma matriz de distâncias e encontra o caminho mais curto entre as localizações fornecidas.
Retornando para o Usuario uma tabela das rotas ordenadas, e a possibilidade de abrir a rota no Google Maps.

## Índice

1. [Estrutura do Código](#estrutura-do-código)
   - [main.py](#mainpy)
   - [controller.py](#controllerpy)
   - [templates/](#templates)
   - [static/](#static)
2. [Arquitetura da Aplicação](#arquitetura-da-aplicação)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Funcionalidades](#funcionalidades)
5. [Exemplo de Uso](#exemplo-de-uso)
6. [Instalação](#instalação)
   - [Pré-requisitos](#pré-requisitos)
   - [Passos para Configuração](#passos-para-configuração)
7. [Contribuições](#contribuições)
8. [Licença](#licença)


## Estrutura do Código

***main.py:*** O arquivo principal da aplicação onde o FastAPI é inicializado e as rotas são definidas.

***controller.py:*** Contém funções para calcular a matriz de distâncias e encontrar a rota mais curta.

***templates/:*** Diretório contendo os templates HTML.

***static/:*** Diretório para arquivos estáticos (CSS, JS, imagens).

```
Route-Otimization/
│
├── main.py          # Arquivo principal da aplicação
├── controller.py    # Funções para manipulação de rotas e distâncias
├── templates/       # Diretório para templates HTML
│   ├── index.html
│   └── result.html
└── static/          # Diretório para arquivos estáticos (CSS, JS, etc.)
```

## Arquitetura da Aplicação

![image](https://github.com/user-attachments/assets/5dda8f50-15df-470b-8609-3f5960b31947)

A arquitetura da aplicação é baseada em uma estrutura MVC (Model-View-Controller):

- **Model**: Utiliza a API do Google Maps para obter a matriz de distâncias entre as cidades.
- **View:** Renderiza as páginas HTML utilizando Jinja2, exibindo os resultados da rota calculada.
- **Controller:** Gerencia a lógica de negócios, incluindo o cálculo da menor rota e a construção da matriz de distâncias.

A comunicação entre esses componentes é feita de forma organizada, garantindo a separação de responsabilidades e facilitando a manutenção do código.

### Tecnologias Utilizadas

- **FastAPI**: Framework para construção de APIs rápidas.
- **Google Maps API**: Para obtenção de distâncias entre as cidades.
- **Pandas**: Para manipulação de dados e criação de tabelas.
- **Jinja2**: Para renderização de templates HTML.

### Funcionalidades

- Insira sua origem e múltiplos destinos.
- Calcula a rota mais curta e a distância total.
- Gera uma URL do Google Maps para a rota.

### Exemplo de Uso

1. Navegue até a página principal e preencha os campos de origem e destino.
2. Envie o formulário para ver a rota calculada e a distância total.
3. Clique no link gerado do Google Maps para obter direções.
   
## Instalação

### Pré-requisitos

- Python 3.9 ou superior
- Uma chave da API do Google Maps

### Passos para Configuração

1. **Clone o repositório:**

    ```bash
     git clone <url_do_repositório>
     cd Route-Otimization
    ```

2. ***Crie um ambiente virtual:***

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`.
    ```

3. ***Instale os pacotes necessários:***

    ```bash
    pip install -r requirements.txt
    ```

4. ***Configure sua chave da API do Google Maps:***

    Crie um arquivo .env na raiz do projeto e adicione sua chave da API:
  
      ```env
      GOOGLE_KEY=sua_chave_da_api_google_maps
      ```

5. ***Execute a aplicação:***

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

6. ***Acesse a aplicação:***

    Abra seu navegador e navegue até http://localhost:8000.

## Contribuições
Sinta-se à vontade para contribuir com o projeto! Faça um fork, crie uma branch para sua feature e envie um pull request. Ajude a melhorar essa aplicação!
Entre em contato comigo para que possamos contribuir em features juntos (https://www.linkedin.com/in/jpcamatari/)

## Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
