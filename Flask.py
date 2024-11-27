from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        verify_token = "my_new_verify_token"
        if request.args.get('hub.verify_token') == verify_token:
            return request.args.get('hub.challenge'), 200
        return "Unauthorized", 403
    return "Webhook received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
