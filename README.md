## Integração de IA com OpenAI Usando Flask  

Este projeto utiliza a API da OpenAI para criar uma aplicação web que responde a perguntas utilizando modelos avançados de processamento de linguagem natural. Veja abaixo as funcionalidades principais e instruções detalhadas.

---

### **⚠️ Atenção: Créditos da API**  
Para utilizar este projeto, é necessário ter uma **chave de API da OpenAI** e créditos suficientes na conta. Sem créditos, as solicitações à API não funcionarão.  

- Verifique seus créditos acessando sua conta em [OpenAI Platform](https://platform.openai.com/account/usage).  
- Certifique-se de ter saldo disponível antes de testar a aplicação.  

---

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
     - [Documentação do Python-dotenv](https://pypi.org/project/python-dotenv/)

5. **Verifique se os Créditos da API estão Disponíveis**:  
   - Certifique-se de que sua conta possui créditos suficientes para evitar interrupções no serviço.  

6. **Executando o Código**:  
   - Instale as bibliotecas necessárias:  
     ```  
     pip install Flask openai  
     ```  
     - [Documentação do Flask](https://flask.palletsprojects.com/)  
     - [Documentação da OpenAI Python API](https://platform.openai.com/docs/overview)  
   - Execute o aplicativo Flask com:  
     ```  
     python app.py  
     ```  
   - O servidor Flask será iniciado e estará disponível em `http://localhost:5000`.  

---

### Erros Comuns e Como Resolver

1. **Erro: "API Key inválida"**
   - Verifique se a chave da API foi copiada corretamente e se está configurada no arquivo `.env`.
   - Certifique-se de que sua chave está ativa e com créditos suficientes na [plataforma da OpenAI](https://platform.openai.com/account/usage).

2. **Erro: "ModuleNotFoundError: No module named 'openai'"**
   - Isso significa que a biblioteca `openai` não está instalada. Execute o comando:
     ```
     pip install openai
     ```

3. **Erro: "Não foi possível se conectar ao servidor"**
   - Verifique sua conexão com a internet e a disponibilidade da API da OpenAI.

---

### Links Úteis  
- [Documentação da API da OpenAI](https://platform.openai.com/docs/overview)  
- [Documentação do Flask](https://flask.palletsprojects.com/)  
- [Documentação do Python-dotenv](https://pypi.org/project/python-dotenv/)
