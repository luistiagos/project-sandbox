from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notification', methods=['POST'])
def notification():
    payment_info = request.get_json()
    email = payment_info['payer']['email']
    print(f"Received payment notification for {email}")
    return jsonify(success=True)

@app.route('/')
def teste():
    return "Teste"

if __name__ == '__main__':
    app.run()