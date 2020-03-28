from flask import Blueprint, json, request

from app import app
from api.make_pass import create_pass

blueprint = Blueprint('api_pass', __name__)


@app.route('/get_pass', methods=['POST'])
def password():
    data = json.loads(request.data)
    new_passs = create_pass(**data)
    response = app.response_class(
        response=json.dumps({'password': new_passs}),
        status=200,
        mimetype='application/json'
    )
    return response
