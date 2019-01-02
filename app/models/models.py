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

import re
from random import randint
from datetime import date

class User:
    """
    Models for the user of the
    application
    """

    user_count=1
    def __init__(self, firstname, lastname, email, **kwargs):
        self.id=__class__.user_count
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.password=kwargs['password']
        self.othernames=kwargs['othernames']
        self.phoneNumber=kwargs['phoneNumber']
        self.username=kwargs['username']
        self.registered=date.today()
        self.isAdmin=kwargs['isAdmin']
        self.__class__.user_count+=1

    #class properties

    @property 
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def phoneNumber(self):
        return self._phoneNumber

    #class property setters
    @email.setter
    def email(self,value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Email addresses should follow the pattern something@email.com")
        self._email = value

    @password.setter
    def password(self,value):
        if not re.match(r"",value):
            raise ValueError("Passwords should atleast be 8 characters long have a uppercase\
            character, lowercase character, and a number")
        self._password = value

    @phoneNumber.setter
    def phoneNumber(self,value):
        if not isinstance(value, str):
            raise TypeError("Phone number can only be a string")
        self._phoneNumber = value

    def convert_to_dict(self):
        return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname, 'password':self.password,
                'othernames': self.othernames, 'email': self.email, 'phoneNumber': self.phoneNumber,
                'username': self.username, 'registered':self.registered, 'isAdmin': self.isAdmin}
        

class Incident:
    """
    Models for the redflag/intervention
    records
    """
    counter=1
    def __init__(self, createdBy, incident_type, location, **kwargs):
        self.id= __class__.counter
        self.createdOn=date.today()
        self.createdBy = createdBy
        self.incident_type = incident_type
        self.location=location
        self.status='draft'
        self.images=kwargs['images']
        self.videos=kwargs['videos']
        self.comment=kwargs['comment']
        self.__class__.counter+=1

    #creating the incident type property inorder
    #to use the class setters to validate its type
    @property
    def incident_type(self):
        return self._incident_type

    @incident_type.setter
    def incident_type(self,value):
        if value not in ['red-flag', 'intervention']:
            raise ValueError("Incident type can only be either 'red-flag' or 'intervention'")
        self._incident_type=value

    def convert_data(self):
        return {'id': self.id, 'createdOn':self.createdOn, 'createdBy': self.createdBy, 
                'incident_type': self.incident_type, 'location':self.location, 'status':self.status, 
                'images':self.images, 'videos':self.videos, 'comment':self.comment}
