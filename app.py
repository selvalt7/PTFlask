from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/book/<id>')
def book(id):
  return render_template(f'k{id}.html')

if __name__ == '__main__':
  app.run(debug=True)