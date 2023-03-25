from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cuba')
def cuba():
    return render_template('cuba.html', tahun='2023')


if __name__ == "__main__":
    app.run()
