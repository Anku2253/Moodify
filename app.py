from flask import Flask, render_template, request
import requests

URL = 'https://zenquotes.io/api/random/'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    quote = None
    if request.method == 'POST':
        try:
            response = requests.get("https://zenquotes.io/api/random")
            data = response.json()
            quote = data[0]['h']  # Use preformatted HTML
        except Exception as e:
            quote = "<i>Something went wrong. Try again later.</i>"

    return render_template('generator.html', quote=quote)


if __name__ == "__main__":
    app.run(debug=True)
