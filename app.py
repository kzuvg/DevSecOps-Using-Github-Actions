from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is UP and RUNNING'


app.run(port=80)
