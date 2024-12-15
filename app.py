# app.py
from flask import Flask, render_template
from Controllers.BukuController import index,db  # Panggil fungsi dari controller
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Membuat rute baru
@app.route('/')
def home():
    return render_template('Home.html')  # Pastikan Anda memiliki file template Home.html

# Rute buku
@app.route('/buku')
def buku():
    items = index()  # Panggil fungsi controller untuk mendapatkan data
    return render_template('Buku.html', items=items)

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
