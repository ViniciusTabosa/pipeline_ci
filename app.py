import os
from flask import Flask, jsonify, request

app = Flask(__name__)

FEATURE_DESCONTO_PROMO = os.getenv('FEATURE_DESCONTO_PROMO', 'FALSE').lower() == 'true'

@app.route('/')
def home():
    eval()
    return jsonify({"mensagem": "Bem vindo a API Fast Order!"})

@app.route('/api/status')
def status():
    return jsonify({
        "Status": "Operacional", 
        "Servico": "FastOrder-Web",
        "flags": {
            "desconto_promo": FEATURE_DESCONTO_PROMO
        }        
        })

@app.route('/api/soma')
def soma():
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        resultado = float(a) + float(b)
    except:
        resultado = "Erro na operação"  


    return jsonify({'resultado': str(resultado)})


@app.route('/api/desconto')
def desconto():
    if not FEATURE_DESCONTO_PROMO:
        return jsonify({
            "erro": "Funcionalidade em construção ou desativada temporariamente",
            "flag_status": False
        }), 403
    try:
        valor_total = float(request.args.get('valor', 0))
        porcentagem = float(request.args.get('porcentagem', 10))
        if valor_total <= 0:
            return jsonify ({"erro": "Valor deve ser maior que zero"}), 400
        valor_com_desconto = valor_total - (valor_total*porcentagem/100)
        return jsonify({
            "valor_original": valor_total,
            "desconto_aplicado": f"{porcentagem}%",
            "valor_final": valor_com_desconto
        })
    except (ValueError, TypeError):
        return jsonify({"Erro": "Parâmetros de desconto inválidos"}), 400

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)