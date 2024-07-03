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
    
    # Gerar resposta com histórico completo
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
