from flask import Flask, render_template
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.route("/")
def home():
    return render_template("index.html", api_key=API_KEY)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)