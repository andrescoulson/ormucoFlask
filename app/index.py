from flask import Flask
from flask import render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.exc import InvalidRequestError, SQLAlchemyError

from database import db, Datos
import config

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES



db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def hello():
    dato = Datos.query.all()
    if request.method == 'POST':
        try:
            nombre = str (request.form['name'])
            nombre = nombre.capitalize()
            datos = Datos(nombre, request.form['color'], request.form['cats_dogs'])
            db.session.add(datos)
            db.session.commit()
            dato = Datos.query.all()
            return render_template('index.html', dato=dato)
        except (InvalidRequestError):
            print db.session.rollback()
        except Exception as ex:
            print ex


    return render_template('index.html', dato=dato)


if __name__ == "__main__":
    app.run(debug=True)
