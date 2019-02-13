from flask import Flask, Blueprint, request, make_response, jsonify
import json
from app.utils.validations import check_office_keys, raise_error
from app.api.v1.model.office_model import OfficeModel, office_list
my_v1= Blueprint('office',__name__, url_prefix='/api/v1')


    
@my_v1.route('/office', methods=['POST'])
def createOffice():
    data = request.get_json()
    error = check_office_keys(data)
    if error:
        return raise_error( 400, "Invalid {} key".format(', '.join(error)))
        
    if data['name'].isalpha() is False and data['office_type'].isalpha() is False:
        raise_error(400, "Invalid Input try again")
    for office in office_list:
        if office['name'] == data['name'] and data['name'] == " ":
            return raise_error(400, "Office name  already taken try another one")

        if office['office_type']==data['office_type'] and data['office_type']  != " ":
            return raise_error(400, "Office type already taken try another one")

    new_pty=OfficeModel().create_office(data['name'], data['office_type'])
    return make_response(jsonify({
        'msg':"Success"
    }), 201)

@my_v1.route('/office', methods=['GET'])
def getAllOffice():
    offices = OfficeModel().get_all_office()
    return make_response(jsonify({
                    "msg":"Ok",
                'officey': offices        
    }), 200)

@my_v1.route('/office/<int:id>', methods=['GET'])
def getasingleoffice(id):
    if isinstance(id, int):
        office = OfficeModel().getoffice(id)
        return make_response(jsonify({"msg":"Ok",'Office': office }), 200)
    return make_response(jsonify({"msg":"could not find your search",'office': "No office found" }), 404)
    return make_response(jsonify({"msg":"That is not correct id",'Office': id }), 404)


