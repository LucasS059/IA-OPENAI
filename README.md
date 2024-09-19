## Integração de IA com OpenAI Usando Flask

Este projeto utiliza a API da OpenAI para criar uma aplicação web que responde a perguntas utilizando modelos avançados de processamento de linguagem natural. Veja abaixo as funcionalidades principais e instruções detalhadas.

### Funcionalidades

1. **Resposta a Perguntas**: Utilizando o modelo GPT-3.5-turbo da OpenAI, a aplicação gera respostas coerentes e contextuais para perguntas feitas pelos usuários.

2. **Histórico de Conversação**: A aplicação mantém um histórico das interações, exibindo perguntas e respostas de maneira contínua.

### Como Utilizar

1. **Obtenha uma Chave de API da OpenAI**:
   - Acesse [OpenAI Platform](https://platform.openai.com/signup) e crie uma conta, se ainda não tiver uma.
   - Após o login, vá para a seção "API Keys" e crie uma nova chave de API.
   - Copie a chave gerada para uso posterior.

2. **Crie um Arquivo `.env` na Raiz do Projeto**:
   - Na raiz do seu projeto Flask, crie um arquivo chamado `.env` se ainda não existir.

3. **Adicione sua Chave da API ao Arquivo `.env`**:
   - Insira a seguinte linha no arquivo `.env`, substituindo `SuaChaveDaAPIAqui` pela chave obtida:
     ```
     OPENAI_API_KEY=SuaChaveDaAPIAqui
     ```

4. **Configure o Projeto para Usar a Chave da API**:
   - Instale a biblioteca `python-dotenv` com `pip install python-dotenv` para carregar variáveis de ambiente do arquivo `.env`.

5. **Verifique se os Créditos da API estão Disponíveis**:
   - Certifique-se de que sua conta possui créditos suficientes para evitar interrupções no serviço.

6. **Executando o Código**:
   - Instale as bibliotecas necessárias:
     ```
     pip install Flask openai
     ```
   - Execute o aplicativo Flask com:
     ```
     python app.py
     ```
   - O servidor Flask será iniciado e estará disponível em `http://localhost:5000`.

### Código Python

O código abaixo configura um servidor Flask para integrar a API da OpenAI e responder a perguntas dos usuários:

```python
from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
cliente = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
historico = []

@app.route('/')
def home():
    return render_template('index.html', historico=historico)

@app.route('/ChatGpt-Openai', methods=['POST'])
def perguntar():
    pergunta = request.form['question']
    historico.append({"role": "user", "content": pergunta})
    
    resposta = cliente.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=historico,
        temperature=1
    ).choices[0].message.content.strip()

    resposta_formatada = resposta.replace("\n", "<br>") 
    historico.append({"role": "assistant", "content": resposta_formatada})
    return redirect(url_for('home'))

@app.route('/clear', methods=['POST'])
def limpar():
    global historico
    historico = []
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Código HTML

O código HTML a seguir representa a interface do chatbot, com uma experiência de chat limpa e responsiva:

```html
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API - OPENAI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #2c2c2c;
            color: #ffffff;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .chat-container {
            width: 100%;
            max-width: 800px;
            background-color: #1a1a1a;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 80vh;
            position: relative;
        }

        .tema {
            background-color: #333333;
            padding: 15px;
            text-align: center;
            border-bottom: 1px solid #444444;
        }

        .tema h1 {
            margin: 0;
            font-size: 24px;
        }

        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }

        .message {
            margin: 10px 0;
            padding: 15px;
            border-radius: 10px;
            max-width: 80%;
            word-wrap: break-word;
            position: relative;
            background-color: #2c2c2c;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
        }

        .message-user {
            align-self: flex-end;
            background-color: #4a4a4a;
        }

        .message-assistant {
            align-self: flex-start;
            background-color: #333333;
        }

        .message::before {
            content: attr(data-role);
            font-weight: bold;
            font-size: 14px;
            color: #cccccc;
            margin-bottom: 5px;
        }

        .message-user::before {
            color: #4a4a4a;
        }

        .message-assistant::before {
            color: #333333;
        }

        .input-container {
            border-top: 1px solid #444444;
            padding: 10px;
            background-color: #2c2c2c;
            display: flex;
            align-items: center;
        }

        .input-container form {
            display: flex;
            flex: 1;
            align-items: center;
            gap: 10px;
        }

        .input-container textarea {
            flex: 1;
            padding: 12px;
            border: 1px solid #444444;
            background-color: #1a1a1a;
            color: #ffffff;
            font-size: 16px;
            border-radius: 5px;
            resize: none;
            min-height: 60px;
        }

        .buttons {
            display: flex;
            gap: 10px;
        }

        .buttons form {
            margin: 0;
        }

        .input-container button {
            padding: 12px 20px;
            border: none;
            background-color: #4a4a4a;
            color: #ffffff;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .input-container button:hover {
            background-color: #6e6e6e;
        }

        .clear-button {
            background-color: #ff4b4b;
            color: #ffffff;
            border: none;
            padding: 12px 20px;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .clear-button:hover {
            background-color: #ff0000;
        }
    </style>
</head>

<body>
    <div class="chat-container">
        <div class="tema">
            <h1>IA - OPENAI</h1>
        </div>

        <div class="messages">
            {% for mensagem in historico %}
            <div class="message {{ mensagem.role }}" data-role="{{ mensagem.role.capitalize() }}">
                <div>{{ mensagem.content | safe }}</div>
            </div>
            {% endfor %}
        </div>

        <div class="input-container">
            <form action="{{ url_for('perguntar') }}" method="post">
                <textarea name="question" placeholder="Digite sua pergunta" rows="3" required></textarea>
                <div class="buttons">
                    <button type="submit">Enviar</button>
                    <form action="{{ url_for('limpar') }}" method="post" style="display:inline;">
                        <button type="submit" class="clear-button">Apagar Conversa</button>
                    </form>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
```

### Nota Importante

Certifique-se de colocar todos os arquivos HTML na pasta `templates`. O Flask utiliza essa convenção para localizar os templates durante a execução do aplicativo.

---
