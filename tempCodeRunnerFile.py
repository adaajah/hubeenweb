from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json, os

app = Flask(__name__)
app.secret_key = 'rahasia'
DATA_FILE = 'account.json'

# Inisialisasi file user
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Status perangkat global
device_status = {
    "uvlamp": "off",
    "foodbottle": "closed",
    "temperature": "--"
}
# Fungsi bantu: user
def load_users():
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# ROUTING UTAMA (WEB)
@app.route("/")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session["username"])

@app.route("/about")
def about():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("about.html", username=session["username"])

@app.route("/contact")
def contact():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("contact.html", username=session["username"])

# LOGIN / SIGNUP
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()
        for user in users:
            if user["username"] == username and user["password"] == password:
                session["username"] = username
                return redirect(url_for("home"))
        return "Login gagal. Username atau password salah.", 401
    return render_template("login.html")

@app.route("/logout")
def logout():
session.pop("username", None)
return redirect(url_for("login"))

@app.route("/forgot", methods=["GET", "POST"])
return render_template("forgot.html") 
# RUN APP
if __name__ == "__main__":
    app.run(debug=True)