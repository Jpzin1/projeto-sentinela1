# sentinel-server/app.py

from flask import Flask, request

# Cria a aplicação Flask
app = Flask(__name__)

# Define uma rota para o endpoint /ingest que aceita requisições POST
@app.route('/ingest', methods=['POST'])
def ingest_log():
    # Pega o conteúdo JSON da requisição
    data = request.get_json()

    # Imprime os dados recebidos no console do contêiner Docker
    # Esta é a forma mais simples de "ver" os dados chegando
    print("===================================")
    print(f"DADOS RECEBIDOS DO AGENTE:")
    print(data)
    print("===================================")

    # Retorna uma resposta de sucesso
    return {"status": "success", "message": "Data received"}, 200

# Roda a aplicação
if __name__ == '__main__':
    # O host '0.0.0.0' faz o servidor ser acessível de fora do contêiner
    app.run(host='0.0.0.0', port=5000, debug=True)