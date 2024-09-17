## Integração de IA com OpenAI usando Flask

Este projeto utiliza a API da OpenAI para criar uma aplicação web que responde a perguntas utilizando modelos avançados de processamento de linguagem natural. Abaixo estão as funcionalidades principais do código:

### Funcionalidades:

1. **Resposta a Perguntas**: Utilizando o modelo GPT-3.5-turbo da OpenAI, a aplicação é capaz de gerar respostas coerentes e contextuais a perguntas formuladas pelo usuário.

2. **Histórico de Conversação**: A aplicação mantém um histórico das interações entre usuário e bot, exibindo tanto as perguntas feitas quanto as respostas geradas.

### Como Utilizar:

1. **Obtenha uma Chave de API da OpenAI**:
   - Acesse o site da OpenAI Platform em [OpenAI Platform](https://platform.openai.com/signup).
   - Crie uma conta se ainda não tiver uma. Você precisará fornecer um endereço de e-mail válido.
   - Após criar sua conta, faça login na plataforma.
   - No painel principal da OpenAI, procure por opções relacionadas a "API Keys" ou "Your API Keys".
   - Clique para criar uma nova chave de API. Você pode precisar configurar permissões de acesso dependendo do plano que escolher.

2. **Crie um Arquivo `.env` na Raiz do Projeto**:
   - Após obter sua chave de API da OpenAI, crie um arquivo chamado `.env` na pasta raiz do seu projeto Flask, se ainda não existir.

3. **Adicione sua Chave da API ao Arquivo `.env`**:
   - Dentro do arquivo `.env`, adicione a seguinte linha, substituindo `SuaChaveDaAPIAqui` pela chave que você obteve:
     ```
     OPENAI_API_KEY=SuaChaveDaAPIAqui
     ```

   Certifique-se de não incluir aspas ou quaisquer caracteres adicionais além da chave.

4. **Configure o Projeto para Usar a Chave da API**:
   - No código Python do seu projeto Flask, você pode usar a biblioteca `python-dotenv` para carregar automaticamente as variáveis de ambiente definidas no arquivo `.env`. Certifique-se de ter instalado a biblioteca usando `pip install python-dotenv`.

5. **Verifique se os Créditos da API estão Disponíveis**:
   - A API da OpenAI requer a compra de créditos de token para utilização. Após configurar sua chave, verifique se sua conta possui créditos suficientes para evitar interrupções no serviço.

6. **Executando o Código**:
   - Certifique-se de ter as bibliotecas necessárias instaladas. Caso contrário, instale o Flask e a biblioteca OpenAI usando:
     ```
     pip install Flask openai
     ```
   - Execute o aplicativo Flask utilizando o comando:
     ```
     python app.py
     ```
   - O servidor Flask será iniciado e estará disponível em `http://localhost:5000` por padrão, pronto para receber perguntas e fornecer respostas utilizando a inteligência artificial da OpenAI.

### Código Python:

O código Python abaixo demonstra como configurar um servidor Flask para integrar a API da OpenAI e responder a perguntas dos usuários:

```python

from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chave_api_openai = os.getenv('OPENAI_API_KEY')
cliente = OpenAI(api_key=chave_api_openai)

app = Flask(__name__)

historico = []

@app.route('/')
def home():
    return render_template('index.html', historico=historico)

@app.route('/ChatGpt-Openai', methods=['POST'])
def perguntar():
    pergunta = request.form['question']
    historico.append({"role": "user", "content": pergunta})
    resposta = gerar_resposta_pergunta(historico)
    historico.append({"role": "assistant", "content": resposta})
    return redirect(url_for('home'))

@app.route('/clear', methods=['POST'])
def limpar():
    global historico
    historico = []
    return redirect(url_for('home'))

def gerar_resposta_pergunta(historico):
    resposta = cliente.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=historico,
        temperature=1, 
    )

    texto_cru = resposta.choices[0].message.content.strip()
    linhas = texto_cru.split('\n')
    resposta_formatada = '<br>'.join(linhas)
    return resposta_formatada

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

```

### Código HTML:

A página HTML a seguir representa a interface onde o chatbot da OpenAI será exibido. Ela utiliza estilos CSS para criar uma experiência de chat limpa e responsiva:

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
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 80vh; 
            position: relative;
        }

        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }

        .messages p {
            margin: 10px 0;
            padding: 10px 15px;
            border-radius: 8px;
            max-width: 80%;
            word-wrap: break-word;
        }

        .message-user {
            align-self: flex-end;
            background-color: #4a4a4a;
        }

        .message-assistant {
            align-self: flex-start;
            background-color: #333333;
        }

        .input-container {
            display: flex;
            flex-direction: column;
            border-top: 1px solid #444444;
            padding: 10px;
            background-color: #2c2c2c;
        }

        .input-container textarea {
            flex: 1;
            padding: 15px;
            border: none;
            background-color: #2c2c2c;
            color: #ffffff;
            font-size: 16px;
            border-radius: 5px;
            resize: none;
            min-height: 50px;
        }

        .input-container button {
            padding: 15px 20px;
            border: none;
            background-color: #3b3b3b;
            color: #ffffff;
            cursor: pointer;
            font-size: 16px;
            border-radius: 0 5px 5px 0;
        }

        .input-container button:hover {
            background-color: #555555;
        }

        .tema {
            text-align: center;
            margin: 10px; 
            border-radius: 10px;
            background-color: #3b3b3b;
        }

        .clear-button {
            background-color: #ff4b4b;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
            border-radius: 5px;
            margin: 0 auto;
        }

        .clear-button:hover {
            background-color: #ff0000;
        }

        .button_submit {
            margin: 10px;
        }
        
        .forms_clear {
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

    </style>
</head>
<body>

    <div class="chat-container">
        <div class="tema">
            <h1>IA - OPENAI</h1>
        </div>

        <div class="messages">
            {% for message in historico %}
                <p class="message-{{ message.role }}">{{ message.content | safe }}</p>
            {% endfor %}
        </div>
        <form action="/ChatGpt-Openai" method="POST" class="input-container" id="chat-form">
            <textarea name="question" placeholder="Digite sua pergunta" rows="3" required></textarea>
            <button class="button_submit" type="submit">Enviar</button>
        </form>
        <form action="/clear" method="POST" class="forms_clear">
            <button type="submit" class="clear-button">Apagar Conversa</button>
        </form>
    </div>

    <script>
        // Função para rolar a página automaticamente para o final
        function scrollToBottom() {
            var chatContainer = document.querySelector('.messages');
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        // Chamar a função ao carregar a página
        window.onload = function() {
            scrollToBottom();
        };

        // Chamar a função sempre que o formulário for enviado
        document.getElementById('chat-form').addEventListener('submit', function(event) {
            scrollToBottom();
            // Limpar o campo de entrada após o envio
            document.querySelector('textarea').value = '';
        });

        // Impedir que a tecla Enter crie uma nova linha na textarea
        document.querySelector('textarea').addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                document.getElementById('chat-form').submit();
            }
        });

        // Mostrar a animação de carregamento ao enviar o formulário
        document.getElementById('chat-form').addEventListener('submit', function(event) {
            var question = document.querySelector('textarea').value.trim();
            if (question === '') {
                event.preventDefault();
                return;
            }
        });
    </script>
</body>
</html>

```

### Nota Importante:

Para usar o código HTML fornecido no projeto Flask, certifique-se de colocar todos os arquivos HTML na pasta `templates`. O Flask utiliza essa convenção para localizar os templates HTML durante a execução do aplicativo.

---
