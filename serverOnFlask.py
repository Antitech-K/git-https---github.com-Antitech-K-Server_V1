from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # секретный ключ для подписи JWT-токенов
#app.config['STATIC_IP'] = '127.0.0.1:8085'  # статический IP-адрес сервера

# примеры различных запросов, которые может принимать приложение
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    print(auth, type(auth))
    if auth and auth.username == 'username' and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

@app.route('/resource', methods=['GET'])
def resource():
    token = request.headers.get('Authorization').split()[1]
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'message': 'Invalid token'}), 403
    return jsonify({'message': 'Valid token'})

# логирование всех действий приложения в файл
@app.after_request
def after_request(response):
    with open('log.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()} {request.method} {request.path} {response.status}\n')
    return response

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host=app.config['STATIC_IP'], debug=True)