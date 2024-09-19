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
