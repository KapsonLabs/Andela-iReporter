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

incidents=[]

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
            pass

    def post(self):

        try:
            if len(request.json) == 7:
                incident = Incident(request.json['createdBy'], request.json['incident_type'], request.json['location'], 
                status=request.json['status'], Image=request.json['Image'], Videos=request.json['Videos'], 
                comment=request.json['comment'])
                incidents.append(incident)
            else:
                return jsonify({"status":400, "error": "Improper data body, Read documentation to send the appropriate data"})
        except ValueError as e:
            print(e)
            return jsonify({"status":400, "error": "One of the values you posted happens to be of an unsupported\
            type/format. {0}".format(e)})
        return jsonify({"status":201, "data": [{"id":incident.id, "message":"Created Red flag Record"}]})

    def delete(self,id):
        pass

