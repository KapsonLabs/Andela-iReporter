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

from app.models.models import Incident

accounts=[]
incidents=[]

class UserAPI(MethodView):
    def get(self,id):
        pass

    def post(self):
        pass

    def delete(self,id):
        pass

    def patch(self,id):
        pass

class IncidentAPI(MethodView):
    
    def get(self,id):
        if id is None:
            #return all redflags
            redflags = []
            for incident in incidents:
                redflags.append(incident.convert_data())

            if len(incidents) < 1:
                return jsonify({"status":200, "message": "There are no incidents yet, Please create one to continue"})
            return jsonify({"status":200, "data": redflags})
        else:
            #return specific red-flag if id is specified
            unique_red_flag = [red_flag for red_flag in incidents if red_flag.__dict__['id'] == int(id)]
            if not unique_red_flag:
                return jsonify({"status":404, "error":"The redflag you requested doesnt exist"})
            return jsonify({"status":200, "data": [unique_red_flag[0].__dict__]})


    def post(self):

        try:
            if len(request.json) == 6:
                incident = Incident(request.json['createdBy'], request.json['incident_type'], request.json['location'], 
                images=request.json['images'], videos=request.json['videos'], 
                comment=request.json['comment'])
                incidents.append(incident)
            else:
                return jsonify({"status":400, "error": "Improper data body, Read documentation to send the appropriate data"})
        except ValueError as e:
            print(e)
            return jsonify({"status":400, "error": "One of the values you posted happens to be of an unsupportedvtype/format.\
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


