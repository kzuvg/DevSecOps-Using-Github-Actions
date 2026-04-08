from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world)():
  return render_template('index.html')

@app.route('/')
def health():
  return 'Server is UP and RUNNING'

app. run(host= '0.0.0.0', port=80)
