from flask import Flask, Blueprint, request, make_response, jsonify
import json
from app.utils.validations import check_party_keys, raise_error, is_valid_url
from app.api.v1.model.party_model import PartyModel, parties_list

my_v1=Blueprint('party',__name__, url_prefix='/api/v1')



@my_v1.route('/party', methods =['POST'])
def create_party():
    """ function for posting data"""
    data = request.get_json()
    error = check_party_keys(data)
    if error:
        return raise_error( 400, "Invalid {} key".format(', '.join(errors)))
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']
    if not is_valid_url(logoUrl):
        return raise_error(400, "wrong URL fotmat ")
    if data['name'].isalpha() is False and data['hqAddress'].isalpha() is False:
        raise_error(400, "Invalid Name try again")
    for party  in parties_list:
        if party['name']==data['name'] and data['name']== " ":
            return raise_error(400, "Name already taken try another one")

        if party['hqAddress']==data['hqAddress'] and data['hqAddress']== " ":
            return raise_error(400, "Address already taken try another one")
            
        if party['logoUrl']==data['logoUrl'] and data['logoUrl']== " ":
            return raise_error(400, "Try onather url")

    new_pty=PartyModel().save(name, hqAddress, logoUrl)
    return make_response(jsonify({
        'msg':"Success"
    }), 201)

@my_v1.route('/party', methods=['GET'])
def get_all_p():
    """return all parties """
    parties= PartyModel().get_All_Parties()
    return make_response(jsonify({
                "msg":"Ok",
                'party': parties        
        }), 200)
  

@my_v1.route('/party/<int:party_id>', methods=['GET'])
def get_Party(party_id):
    if isinstance(party_id, int):
        party=PartyModel().get_Party(party_id)
        if party:
            return make_response(jsonify({
                'message':'Ok',
                'Party':party
            }), 200)
        
    return make_response(jsonify({
        'message':'Error no such party'
    }), 404)

@my_v1.route('/party/<int:party_id>', methods=['DELETE'])
def remove_party(party_id):
    if isinstance(party_id, int):
        party=PartyModel().remove_party(party_id)
        if party:
            return make_response(jsonify({
                'message':'Ok',
            }), 200)
    return make_response(jsonify({
        'message':'Error party could not be deleted'
    }), 404)

@my_v1.route('/party/<int:party_id>', methods = ['PATCH'])
def Update_party(party_id):
    """the function check if the id is int"""
    
    if isinstance(party_id, int):
        for party in parties_list:
            if party['party_id'] == party_id:
                data = request.get_json()
                party['name'] = data['name']
                return make_response(jsonify({
                    'msg':"Success"
                }), 200)

                update_party = {
                    new_name['name']: data['name']
                }
                parties_list.append(update_party)
                return make_response(jsonify({
                    "status": 200,
                    'success': "updated party {}".format(update_party)
                }))
    return make_response(jsonify({
            'error': "Enter the collect id"
    }), 404)

        




