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
    def __init__(self, firstname, lastname, othernames, email, 
                phoneNumber, username, isAdmin):
        self.id=randint(1,5000)
        self.firstname=firstname
        self.lastname=lastname
        self.othernames=othernames
        self.email=email
        self.phoneNumber=phoneNumber
        self.username=username
        self.isAdmin=isAdmin

    def convert_data(self):
        return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname,
                'othernames': self.othernames, 'email': self.email, 'phoneNumber': self.phoneNumber,
                'username': self.username, 'isAdmin': self.isAdmin}
        

class Incident:
    """
    Models for the redflag/intervention
    records
    """
    def __init__(self, createdBy, incident_type, location, status, Image,
                Videos, comment):
        self.id=randint(1, 1000)
        self.createdOn=date.today()
        self.createdBy = createdBy
        self.incident_type = incident_type
        self.location=location
        self.status=status
        self.Image=Image
        self.Videos=Videos
        self.comment=comment

    def convert_data(self):
        return {'id': self.id, 'createdOn':self.createdOn, 'createdBy': self.createdBy, 
                'incident_type': self.incident_type, 'location':self.location, 'status':self.status, 
                'Image':self.Image, 'Videos':self.Videos, 'comment':self.comment}
