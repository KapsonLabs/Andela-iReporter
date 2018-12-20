"""
Author: Allan Katongole
Date: 19th December 2018
Flask API for iReporter Developer challenge
"""

from flask import Flask, jsonify, request, Response, json
from src.models import User, Incident

app = Flask(__name__)

incidents=[]

@app.route('/')
def hello_world():
    return 'Welcome to Allan iReporter'

# GET incidents
@app.route('/api/v1/red-flags', methods=['GET'])
def get_all_incidents():
    redflags = []
    for incident in incidents:
        redflags.append(incident.convert_data())

    if len(incidents) < 1:
        return jsonify({"status":200, "message": "There are no products"})
    return jsonify({"status":200, "data": redflags})

#POST incident
@app.route('/api/v1/red-flags', methods=['POST'])
def add_incident():
    data = request.get_json()

    try:
        incident = Incident(data['createdBy'], data['incident_type'], data['location'], 
                    data['status'], data['Image'], data['Videos'], data['comment'])
        incidents.append(incident)
    except ValueError as e:
        print(e)
        return jsonify({"status":400, "message": "Price should be integer"})
    return jsonify({"status":201, "data": [incident.convert_data()]})


#GET an incident
@app.route('/api/v1/red-flags/<int:id>', methods=['GET'])
def get_unique_incident(id):
    try:
        redflagss=[]
        print(redflagss)
        for incident in incidents:
            redflagss.append(incident.convert_data())
        for redflag in redflagss:
            if redflag['id'] == id:
                return jsonify({"status":200, "data": redflag})
            else:
                return jsonify({"status":404, "message":"The resource doesnt exist"})
    except AttributeError:
        return jsonify({"status":404, "message":"The data structure is empty, Please Post first"})


#UPDATE an incident
@app.route('/api/v1/red-flags', methods=['PATCH'])
def update_incident_record(id):
    pass


#DELETE an incident
# @app.route('/api/v1/red-flags/<int:id>', methods=['DELETE'])
# def delete_incident_record(id):
#     try:
#         redflagss=[]
#         print(redflagss)
#         for incident in incidents:
#             redflagss.append(incident.convert_data())
#         for redflag in redflagss:
#             if redflag['id'] == id:
#                 return jsonify({"status":200, "data": redflag})
#             else:
#                 return jsonify({"status":404, "message":"The resource doesnt exist"})
#     except AttributeError:
#         return jsonify({"status":404, "message":"The data structure is empty, Please Post first"})

