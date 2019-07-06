#### Flask query string parser
A simple decorator used to validate the required query strings parameters in [Flask](http://flask.pocoo.org).

##### Instalation

Install using  `python setup.py install`

##### Usage

Just add the decorator in your endpoints, the required parameters names and they data types should  be added in a list of tuples.

```
from flask import Flask
from flask_queryparser.query_parser import query_params_parser

app = Flask(__name__)

@app.route("/endpoint")
@query_params_parser([("param1",int),("param2",str)])
def endpoint():
    return "ok!"
```

If your endpoint doesn't get the required parameters, you get the following response:
```
{
    "error": "missing required query strings parameters",
    "missing_parameters": [
        {
            "name": "param1",
            "type": "<class int>"
        },
        {
            "name": "param2",
            "type": "<class str>"
        }
    ]
}
```

TODOS:
1) Add the posibility to add required and optional parameters.
2) Return the parsed parameters in the expected data types.
3) Extend to the possibility of customs messages when parameters are not included