from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    errors = []
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")

        # CHYBA: neověřujeme, zda pole nejsou prázdná
        # CHYBA: email není validován (chybí @)
        # CHYBA: věk může být záporný nebo text

        return render_template("form.html", success=True, name=name, email=email, age=age)

    return render_template("form.html", success=False, errors=errors)

@app.route("/api/submit", methods=["POST"])
def api_submit():
    data = request.get_json()

    name = data.get("name", "")
    email = data.get("email", "")
    age = data.get("age", "")

    # CHYBA: API vždy vrací status 200, i když chybí data
    return jsonify({"message": "Data received", "name": name, "email": email, "age": age}), 200

if __name__ == "__main__":
    app.run(debug=True)
