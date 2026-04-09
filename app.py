from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is UP and RUNNING'


app.run(host='0.0.0.0', port=80)
