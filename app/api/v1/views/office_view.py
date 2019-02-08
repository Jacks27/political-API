from flask import Flask, Blueprint, request, make_response, jsonify
import json
from app.api.v1.model.office_model import OfficeModel

my_v1= Blueprint('v1',__name__, url_prefix='/api/v1')


    
@my_v1.route('/add_office', methods=['POST'])
def createOffice():
    data = request.get_json()
    name = data['name']
    office_type= data['office_type']
    new_pty=OfficeModel().create_office(name, office_type)
    return make_response(jsonify({
        'msg':"Success"
    }), 201)

@my_v1.route('/get_all_offices', methods=['GET'])
def getAllOffice():
    offices = OfficeModel().get_all_office()
    return make_response(jsonify({
                    "msg":"Ok",
                'party': offices        
    }), 200)

@my_v1.route('/get_a_specific_office/<int:id>', methods=['GET'])
def getAsingleOffice(id):
    party_id=isinstance(id, int)
    if party_id:
        office = OfficeModel().getoffice(id)
        return make_response(jsonify({"msg":"Ok",'party': office }), 200)
    return make_response(jsonify({"msg":"That is not correct id",'party': party_id }), 404)


