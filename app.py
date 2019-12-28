import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = "çok gizli key"

# Veri tabanı bağlantısı
uri = os.getenv("MONGO_ATLAS_URI")
client = MongoClient(uri)
db = client.kitaplik.uyeler

"""
app.secret_key = "Çok gizli bir key"
client = MongoClient("mongodb+srv://egitim:egitim48@cluster0-n7pit.mongodb.net/test?retryWrites=true&w=majority")
db = client.fl.flc
"""

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hakkinda')
def hakkinda():
    return render_template('hakkinda.html')
@app.route('/kisisel')
def kisisel():
    return render_template('kisisel.html')
@app.route('/kitaplar')
def kitaplar():
    return render_template('kitaplar.html')
@app.route('/roman')
def roman():
    return render_template('roman.html')
@app.route('/siir')
def siir():
    return render_template('siir.html')
@app.route('/uye')
def uye():
    return render_template('uye.html')
@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

@app.route('/yeniuye')
def yeniuye():
    return render_template('yeniuye.html')

@app.route('/kapat')
def kapat():
    session.pop('eposta', None)
    return redirect('/')

@app.route('/giris',methods=["POST"])
def giris():
  if request.method == 'POST':
        # index.html formundan isim gelecek
        mail = request.form["email"]
        parola = request.form["password"]
        ver=db.find_one({"mail": mail})
        # epostaya ait olan kullanıcı var
        if   ver is not  None :
          if parola == ver.get('parola'):
            # şifre de eşleşiyorsa giriş başarılıdır
            # kullanıcının epostasını session içine al
            session['eposta'] = mail
            # todo ekleyebileceği sayfaya yönlendiriyoruz.
            return redirect('/iletisim')
          else:
            flash("Hatalı şifre girdiniz")
            return render_template('uye.html')
        else:
          flash(f"Sistemde {mail} eposta adresi bulunamadı. Lütfen kayıt olun.")
          return render_template('uye.html')

        
  return render_template('index.html')

@app.route('/kaydol',methods=["POST"])
def kayit():
  if request.method == 'POST':
        # index.html formundan isim gelecek
        ad = request.form["name"]
        mail = request.form["email"]
        parola = request.form["password"]
        soyad = request.form["surname"]
        mydict = { "ad": ad, "mail": mail ,"parola":parola,"soyad":soyad}
        u = db.find_one({'mail':mail})
        if u is None :
                x = db.insert_one(mydict)
                return redirect('/iletisim')
        else:
            flash(f"{mail} eposta adresi daha önceden sistemde kayıtlı")
            return redirect('/')
  return redirect('/')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 