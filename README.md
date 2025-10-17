# 🧮 Calculadora Web com Streamlit

Este projeto é uma calculadora web simples e funcional desenvolvida em Python utilizando a biblioteca **Streamlit** 
## ✨ Funcionalidades

  * **Operações Aritméticas Básicas**:
      * Soma (`+`)
      * Subtração (`-`)
      * Multiplicação (`×`)
      * Divisão (`÷`)
  * **Funções Adicionais**:
      * Cálculo de raízes de equações de segundo grau (Fórmula de Bhaskara).
  * **Interface**:
      * Visor para exibir a expressão atual e o resultado.
      * Layout de botões intuitivo e familiar.
      * Botão 'C' para limpar o visor.
      * Interface limpa e responsiva que se adapta a diferentes tamanhos de tela.

## 🛠️ Tecnologias Utilizadas

  * **[Python 3.8+](https://www.python.org/)**: Linguagem de programação base do projeto.
  * **[Streamlit](https://streamlit.io/)**: Framework open-source para a criação de aplicações web de forma rápida e com poucas linhas de código.

## ⚙️ Pré-requisitos

Antes de começar, você vai precisar ter o [Python](https://www.python.org/downloads/) (versão 3.8 ou superior) e o `pip` (gerenciador de pacotes do Python) instalados em sua máquina.

## 🚀 Instalação e Execução

Siga os passos abaixo para executar o projeto localmente:

**1. Clone o repositório (ou crie o arquivo):**

Primeiro, clone este repositório para a sua máquina local ou simplesmente crie um diretório e salve o código como `app.py`.

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

**2. Crie e ative um ambiente virtual (Recomendado):**

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

**3. Instale as dependências:**

A única dependência externa deste projeto é o Streamlit.

```bash
pip install streamlit
```

**4. Execute a aplicação:**

Com o ambiente virtual ativado, execute o seguinte comando no seu terminal:

```bash
streamlit run app.py
```

Seu navegador abrirá automaticamente no endereço `http://localhost:8501` com a aplicação da calculadora rodando.

## 📂 Estrutura do Arquivo

O projeto é contido em um único arquivo para simplicidade:

  * `app.py`: Contém todo o código da aplicação, incluindo:
      * A classe `Backend` com a lógica dos cálculos.
      * Todo o código do `Frontend` com Streamlit para renderizar a interface e gerenciar as interações do usuário.

## 👨‍💻 Autor

Feito por **[Anderson Felipe Dias Domingos]**.
