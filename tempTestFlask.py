from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)

#Создание базы данных SQLite
def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Child(
                id INTEGER,
                accuracy INTEGER,
                altitude INTEGER,
                altitudeAccuracy INTEGER,
                heading INTEGER,
                latitude REAL,
                longitude REAL,
                speed REAL,
                timeStamp REAL,
                date_time INTEGER)
                ''')
    print("dataBase CREATE")
    cursor.close()
    #conn.close()



#Обработка POST-запросов
@app.route('/child', methods=['GET', 'POST'])
def child():
    print("входящий запрос", request.form)
    print("входящий заголовок", request.headers)
    if request.method == 'POST':
        idDB = request.form.get('id', False)
        accuracy = request.form.get('accuracy', False)
        altitude = request.form.get('altitude', False)
        altitudeAccuracy = request.form.get('altitudeAccuracy', False)
        heading = request.form.get('heading', False)
        latitude = request.form.get('latitude', False)
        longitude = request.form.get('longitude', False)
        speed = request.form.get('speed', False)
        timeStamp = request.form.get('timeStamp', False)

        data_tuple = (idDB, accuracy, altitude, altitudeAccuracy, heading, latitude, longitude, speed, timeStamp)


        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO Child
                    (id, accuracy, altitude, altitudeAccuracy, heading, latitude, longitude, speed, timeStamp, date_time)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now', '+3 hours'))""", data_tuple)
        conn.commit()
        res = cursor.execute("SELECT * FROM Child")
        conn.commit()
        print(res.fetchall())
        conn.close()

        return 'Что-то пришло или вернулось'
    
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        type = request.form['type']
        data_tuple = (phone, type)
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
                    "INSERT INTO Users(phone, type, date_time) VALUES (?, ?, datetime('now', '+3 hours'))", data_tuple )
        conn.commit()
        res = cursor.execute("SELECT * FROM Users")
        conn.commit()
        print(res.fetchall())
        conn.close()
        return "прокатило"
    else:
        return "Не прокатило"

'''
        #Проверка логина и пароля
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT id FROM users WHERE login = '{login}'")
            result = cursor.fetchone()
            if result is None:
                return json.dumps({'error': 'Invalid login'})
            else:
                cursor.execute(f"SELECT password FROM users WHERE id = {result[0]}")
                result = cursor.fetchone()[0]
                if result != password:
                    return json.dumps({'error': 'Incorrect password'})
                else:
                    #Запись логина и пароля в базу данных
                    with conn.cursor() as cursor:
                        cursor.execute('UPDATE users SET password = ? WHERE id = ?', (password, result[0]))
                        conn.commit()
                        response = jsonify({'success': 'Login successful'})
                        return response
    else: 
        return 'Method not allowed'
                
    
'''
    
if __name__ == '__main__':
    create_database()
    app.run(host="0.0.0.0", port=11233, debug=True)
