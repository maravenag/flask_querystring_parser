from flask import Flask
from flask_queryparser.query_parser import query_params_parser

app = Flask(__name__)

@app.route("/endpoint")
@query_params_parser([("param1",int),("param2",str)])
def endpoint():
    return "ok!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)