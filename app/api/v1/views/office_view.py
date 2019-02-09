from flask import Flask, Blueprint, request, make_response, jsonify
import json
from app.api.v1.model.office_model import OfficeModel
my_v1= Blueprint('office',__name__, url_prefix='/api/v1')


    
@my_v1.route('/office', methods=['POST'])
def createOffice():
    data = request.get_json()
    name = data['name']
    office_type= data['office_type']
    new_pty=OfficeModel().create_office(name, office_type)
    return make_response(jsonify({
        'msg':"Success"
    }), 201)

@my_v1.route('/office', methods=['GET'])
def getAllOffice():
    offices = OfficeModel().get_all_office()
    return make_response(jsonify({
                    "msg":"Ok",
                'party': offices        
    }), 200)

@my_v1.route('/office/<int:id>', methods=['GET'])
def getasingleoffice(id):
    if isinstance(id, int):
        office = OfficeModel().getoffice(id)
        return make_response(jsonify({"msg":"Ok",'Office': office }), 200)
    return make_response(jsonify({"msg":"could not find your search",'office': "No office found" }), 404)
    return make_response(jsonify({"msg":"That is not correct id",'Office': id }), 404)


