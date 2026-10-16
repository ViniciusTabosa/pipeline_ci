from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
  return jsonify({"mensagem": "Bem-vindo a API FastOrder!"})

@app.route('/api/status')
def status():
  return jsonify({"status":"operacional", "serviço": "FastOrder"})

@app.route('/api/soma', methods=['GET'])
def soma():
  n1 = int(request.args.get('n1'))
  n2 = int(request.args.get('n2'))
  
  return jsonify({"soma": n1+n2})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)