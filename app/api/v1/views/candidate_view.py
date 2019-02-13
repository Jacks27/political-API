import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.model.candidate_model import CandidateModel, candidates_list
from app.utils.validations import raise_error, \
    check_candidates_keys, on_success
my_v1 = Blueprint('candidates', __name__, url_prefix='/api/v1/')

@my_v1.route("/candidates", methods=["POST"])
def post():
    """Add candidate to the db """
    data= request.get_json()
    error=check_candidates_keys(data)
    if error:
        return raise_error( 400, "Invalid {} key".format(', '.join(error)))
    if isinstance(data['office'], int) is False and isinstance(data['party'], int) is False and \
        isinstance(data['candidate'], int):
        raise_error(400, "Invalid Input try again")
    for office in candidates_list:
        if office['office'] == data['office'] and data['office'] == " ":
            return raise_error(400, "Office name  already taken try another one")

        if office['party']==data['party'] and data['party']  != " ":
            return raise_error(400, "Office type ID already taken try another one")

        if office['candidate']==data['candidate'] and data['candidate']  != " ":
            return raise_error(400, "Office type already taken try another one")

    new_pty=CandidateModel().create_candidates(data['office'], data['party'], data['candidate'])
    return make_response(jsonify({
        'msg':"Success"
    }), 201)
