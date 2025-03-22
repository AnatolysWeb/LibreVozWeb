from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para comunicación con el frontend

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(100), unique=True, nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Modelo de post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

# Ruta para registrar usuarios
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        alias=data['alias'],
        correo=data['correo'],
        password=data['password']  # En producción, se debe cifrar
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado"}), 201

# Ruta para obtener posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"autor": p.autor, "contenido": p.contenido} for p in posts])

# Ruta para crear un post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    nuevo_post = Post(autor=data['autor'], contenido=data['contenido'])
    db.session.add(nuevo_post)
    db.session.commit()
    return jsonify({"mensaje": "Post creado"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)
