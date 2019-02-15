
import os
import datetime
from flask import Blueprint, request, jsonify, abort, make_response
from app.api.v2.models.database import DatabaseConnection as db_conn
from app.api.v2.models.user_model import User
v2_blue = Blueprint("ap1v2", __name__)
KEY = os.getenv("SECRET")
my_v2 = Blueprint('users', __name__, url_prefix='/api/v2/')

@my_v2.route("/signup", methods=["POST"])
def user_signup():

  """endpoint for user to create account """
  try:
    data = request.get_json()

    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    Email = data['Email']
    phoneNumber = data['phoneNumber']
    passportUrl = data['passportUrl']
    password =data['password']
  except Exception:
    return jsonify({
      "error" : "invalid user data input",
      "message" : "missing field",
      "status" : 400
    }), 400

  new_user = User([firstname, lastname, othername, Email, phoneNumber, passportUrl, password])     
  new_user.create_new_user()
  return make_response(jsonify({
  "status": 201, 
  "message": "user created successfully"
  }), 201)
# @my_v2.route("/signup", methods=["POST"])

  