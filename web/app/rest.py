import sys
sys.path.append('/opt/pvviewer/lib/web/app')
import uuid
from flask import Flask, Blueprint, jsonify

from blueprints.api import api

main = Flask(__name__)
main.config['SECRET_KEY'] = uuid.uuid4().hex
main.url_map.strict_slashes = False
main.register_blueprint(api)

def build_error_response(err):
    return {"error": {"type": err.__class__.name, "message": str(err)}}

@main.errorhandler(Exception)
def main_error(err):
    e = build_error_response(err)
    response = jsonify(e)
    try:
        response.status_code = err.errcode
    except:
        response.status_code = 500
    return response

@main.route('/alive')
def get_app_alive():
    return jsonify({})

@main.route('/ready')
def get_app_ready():
    return jsonify({})

if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8080)