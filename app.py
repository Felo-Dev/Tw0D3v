from flask import Flask, render_template, request, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("login.html")
    
    @app.route('/consultar_usuario', methods=['POST'])
    def consultar_usuario():
        """ datos = request.json
        usuario = datos.get('usuario') """
        """   resultado = {usuario} """
        resultado =  "hola mundo" 
        # Devolver la respuesta como JSON
        return jsonify(resultado)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
