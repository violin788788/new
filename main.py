from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("usa.html")
    #return render_template("sweden.html")

if __name__ == "__main__":
    app.run(debug=True, port=5002)

    #http://127.0.0.1:5002/
