"""
Author: Allan Katongole
Date: 19th December 2018
PROJECT: ANDELA iReporter
-----------------------------
Models file for unpersistent
data storage for the flask
API
-----------------------------
"""

from random import randint
from datetime import date

class User:
    """
    Models for the user of the
    application
    """
    def __init__(self, firstname, lastname, email, **kwargs):
        self.id=randint(1,5000)
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.othernames=kwargs['othernames']
        self.phoneNumber=kwargs['phoneNumber']
        self.username=kwargs['username']
        self.isAdmin=kwargs['isAdmin']

    def convert_data(self):
        return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname,
                'othernames': self.othernames, 'email': self.email, 'phoneNumber': self.phoneNumber,
                'username': self.username, 'isAdmin': self.isAdmin}
        

class Incident:
    """
    Models for the redflag/intervention
    records
    """
    def __init__(self, createdBy, incident_type, location, **kwargs):
        self.id=randint(1, 1000)
        self.createdOn=date.today()
        self.createdBy = createdBy
        self.incident_type = incident_type
        self.location=location
        self.status=kwargs['status']
        self.Image=kwargs['Image']
        self.Videos=kwargs['Videos']
        self.comment=kwargs['comment']

    #creating the created by property inorder
    #to use the class setters to validate its type
    @property
    def createdBy(self):
        return self._createdBy

    #validating the type of created by using a setter.
    @createdBy.setter
    def createdBy(self,value):
        if not isinstance(value, str):
            raise ValueError("Created by can only be a string")
        self._createdBy = value

    @property
    def incident_type(self):
        return self._incident_type

    @incident_type.setter
    def incident_type(self,value):
        if not isinstance(value, str):
            if value is not 'red-flag' or 'intervention':
                raise ValueError("Incident type can only be either 'red-flag' or 'intervention'")
            self._incident_type=value

    def convert_data(self):
        return {'id': self.id, 'createdOn':self.createdOn, 'createdBy': self.createdBy, 
                'incident_type': self.incident_type, 'location':self.location, 'status':self.status, 
                'Image':self.Image, 'Videos':self.Videos, 'comment':self.comment}
