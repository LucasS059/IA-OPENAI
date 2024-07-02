from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY') 
client = OpenAI(api_key=openai_api_key)

app = Flask(__name__)

history = []

@app.route('/')
def home():
    return render_template('index.html', history=history)

@app.route('/ChatGpt-Openai', methods=['POST'])
def ask():
    question = request.form['question']
    response = generate_question_response(question)
    
    history.append({"role": "user", "content": question})
    history.append({"role": "bot", "content": response})
    
    return render_template('index.html', history=history)

def generate_question_response(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": question},
        ],
        temperature=0, 
    )

    raw_text = response.choices[0].message.content.strip()

    lines = raw_text.split('\n')
    formatted_response = '<br>'.join(lines)
    
    return formatted_response



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
