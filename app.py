from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('Index.html')

@app.route('/Projeto')
def projeto():
    return render_template('Projeto.html')

@app.route('/Estudo')
def estudo():
    return render_template('Estudos.html')  

@app.route('/Sobre')
def sobre():
    return render_template('Sobre.html')


if __name__ == "__main__":
    app.run(debug=True)

