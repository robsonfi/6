from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculadora', methods=['POST'])
def calculadora():
    dados = request.json
    operacao = dados.get('operacao')
    numero1 = dados.get('numero1')
    numero2 = dados.get('numero2')
    
    if operacao == 'soma':
        resultado = numero1 + numero2
    elif operacao == 'subtracao':
        resultado = numero1 - numero2
    elif operacao == 'multiplicacao':
        resultado = numero1 * numero2
    elif operacao == 'divisao':
        if numero2 == 0:
            return jsonify({"erro": "Divisão por zero não é permitida"}), 400
        resultado = numero1 / numero2
    else:
        return jsonify({"erro": "Operação inválida"}), 400
    
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
