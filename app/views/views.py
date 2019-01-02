"""
Author: Allan Katongole
Date: 28th December 2018
Views for the flask API
of the iReporter challenge.
---------------------------
Most of the logic is run or
implemented here.
---------------------------
Flask pluggable views will be
used as opposed to procedural
programming.
"""

from flask import jsonify, request, Response, json
from flask.views import MethodView

from app.models.models import User, Incident
# from app.utils.utils import requires_admin_access


accounts=[]
incidents=[]

class UserAPI(MethodView):
    """
    class for user account
    management
    """
    # decorators = [requires_admin_access]
    users=[]
    def __init__(self):
        for account in accounts:
            __class__.users.append(account.convert_to_dict())

    def get(self,id):
        if len(accounts) < 1:
            return jsonify({"status":200, "message": "There are no registered users yet"})
        elif id is None:
            #return all redflags
            return jsonify({"status":200, "data": __class__.users})
        else:
            #return specific red-flag if id is specified
            unique_user = [user for user in __class__.users if user['id'] == int(id)]
            if not unique_user:
                return jsonify({"status":404, "error":"The user you requested doesnt exist"})
            return jsonify({"status":200, "data": [unique_user[0]]})

    def post(self):
        try:
            if len(request.json) == 8 and all(isinstance(i, str) for i in [request.json['firstname'], request.json['lastname'],
            request.json['othernames'], request.json['username']]):
                user_account = User(request.json['firstname'], request.json['lastname'], request.json['email'], 
                password=request.json['password'], othernames=request.json['othernames'], phoneNumber=request.json['phoneNumber'],
                username=request.json['username'], isAdmin=request.json['isAdmin'])

                accounts.append(user_account)
            else:
                return jsonify({"status":400, "error": "Improper data body, Read documentation to send the appropriate data"})
        except ValueError as e:
            return jsonify({"status":400, "error": "One of the values you posted happens to be of an unsupported type/format.\
            {0}".format(e)})
        return jsonify({"status":201, "data": [{"id":user_account.id, "message":"Successfully created user"}]})

    def delete(self,id):
        pass

    def patch(self,id):
        pass

class AuthenticationAPI(MethodView):
    """
    class for user account
    authentication management
    """

    def post(self):
        pass

    def delete(self):
        pass

class IncidentAPI(MethodView):
    """
    class that handles the creation
    and management of red-flags
    """
    redflags=[]

    def __init__(self):
        for incident in incidents:
            __class__.redflags.append(incident.convert_data())
    
    def get(self,id):
        if len(incidents) < 1:
            return jsonify({"status":200, "message": "There are no incidents yet"})
        elif id is None:
            #return all redflags
            return jsonify({"status":200, "data": __class__.redflags})
        else:
            #return specific red-flag if id is specified
            unique_red_flag = [red_flag for red_flag in __class__.redflags if red_flag['id'] == int(id)]
            if not unique_red_flag:
                return jsonify({"status":404, "error":"The redflag you requested doesnt exist"})
            return jsonify({"status":200, "data": [unique_red_flag[0]]})


    def post(self):
        try:
            if len(request.json) == 6 and all(isinstance(i, list) for i in [request.json['location'],
            request.json['images'], request.json['videos']]):
                incident = Incident(request.json['createdBy'], request.json['incident_type'], request.json['location'], 
                images=request.json['images'], videos=request.json['videos'], comment=request.json['comment'])
                incidents.append(incident)
            else:
                return jsonify({"status":400, "error": "Improper data body, Read documentation to send the appropriate data"})
        except ValueError as e:
            print(e)
            return jsonify({"status":400, "error": "One of the values you posted happens to be of an unsupported or type/format.\
             {0}".format(e)})
        return jsonify({"status":201, "data": [{"id":incident.id, "message":"Created Red flag Record"}]})

    def delete(self,id):
        try:
            get_record = [incident for incident in incidents if incident.__dict__['id'] == int(id)]
            incidents.remove(get_record[0])
            return jsonify({"status":200, "data": [{"id":get_record[0].id, 
            "message":"Red-flag record deleted successfully"}]}) 
        except:
            return jsonify({"status":404 , "error":"The resource doenot exist"})

    def patch(self,id):
        pass


