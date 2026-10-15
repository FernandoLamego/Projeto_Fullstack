from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# CLIENTES = [
#     {"id": 1, "nome": "Alice", "email": "alice@example.com"},
#     {"id": 2, "nome": "Bob", "email": "bob@example.com"},
#     {"id": 3, "nome": "Charlie", "email": "charlie@example.com"},
#     {"id": 4, "nome": "David", "email": "david@example.com"},
#     {"id": 5, "nome": "Eve", "email": "eve@example.com"}
# ]

CLIENTES = #...banco de dados SQLite ou outra fonte de dados que você deseja usar para armazenar os clientes

#pagina inicial(buscador)
@app.route("/")
def index():
    return render_template("index.html", nome="Buscador de Programas")

@app.route("/api/search", methods=["GET"])
def search_api():
    #criar uma barra de pesquisa, cada letra que digitada,
    #o programa deve buscar na API e mostrar os resultados em tempo real
        
    query = request.args.get("q", "").lower()

    # Se a pesquisa estiver vazia, retorna uma lista vazia
    if not query:
        return jsonify([])

    # Filtra os dados buscando termos relevantes (que contêm a letra/palavra)
    resultados = [
        item for item in CLIENTES if query in item["nome"].lower()
    ]

    # Retorna os resultados mais relevantes em formato JSON
    return jsonify(resultados[:5])  # Limita aos 5 mais relevantes

#pagina de formulario(login com SQLite)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form["username"]
        senha = request.form["password"]
        # Lógica para verificar credenciais no banco de dados
        # ...

    return render_template("login.html", nome="Login")

#pagina de um programa
@app.route("/programa")
def programa():
    return render_template("programa.html", nome="Programa")

#encontrar cliente por id
@app.route("/cliente/<int:id>")
def encontrar_cliente(id):
    for cliente in CLIENTES:
        if cliente["id"] == id:
            return jsonify(cliente)
        return jsonify({"mensagem": "Cliente não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
