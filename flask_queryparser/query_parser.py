from functools import wraps
from flask import request, jsonify

def make_error_message(missing_params):
    return {
        "error": "missing required query strings parameters",
        "missing_parameters":[
            {"name":param[0], "type": "{0}".format(param[1]).replace("'", "")} \
                                                        for param in missing_params
            ]
    }

def query_params_parser(query_params=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            missing_params = []
            for param in query_params:
                param_name, param_type = param[0],param[1]
                try:
                    input_param = request.args.get(param_name)
                    if input_param == None:
                        missing_params.append((param_name, param_type))
                    else:
                        input_param = param_type(input_param) 
                        if isinstance(input_param, param_type):
                            pass
                        else:
                            missing_params.append((param_name, param_type))
                except Exception as e:
                    missing_params.append((param_name, param_type))
            if len(missing_params) > 0:
                return jsonify(make_error_message(missing_params))
            return func(*args, **kwargs)
        return wrapper
    return decorator