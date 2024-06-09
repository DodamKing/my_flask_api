from flask import Flask
from rebalancing_calculator.routes import rc

app = Flask(__name__)

app.register_blueprint(rc, url_prefix='/api/rebalancing-calculator')

@app.route('/')
def hello_word():
    return 'my api server is good!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)