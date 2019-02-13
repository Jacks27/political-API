import re
from flask import jsonify, make_response
def raise_error(status, msg):
    """Handles error messages."""
  
    return make_response(jsonify({
            "status": "error",
            "message": msg
        }), status)

def check_party_keys(data):
    """Check if the key values are correct."""

    res_keys = ['name', 'hqAddress', 'logoUrl']
    errors = []
    for key in res_keys:
        if not key in data.keys():
            errors.append(key)
    return errors

def check_office_keys(data):
    """Check if the key values are correct."""

    res_keys = ['name', 'office_type']
    errors = []
    for key in res_keys:
        if not key in data.keys():
            errors.append(key)
    return errors

def is_valid_url(variable):
   """Check if email is a valid mail."""

   if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
               variable):
       return True
   return False

def is_valid_date(variable):
   """Check if email is a valid mail."""
   
   if re.match(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",
               variable):
       return True
   return False
def on_success(status, msg):
    """Handles error messages."""
  
    return make_response(jsonify({
            "message": msg
        }), status)
def check_candidates_keys(data):
    """Check if the key values are correct."""

    res_keys = ['office', 'party', 'candidate']
    errors = []
    for key in res_keys:
        if not key in data.keys():
            errors.append(key)
    return errors
