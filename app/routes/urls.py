"""
Author: Allan Katongole
Date: 28th December 2018
Routes for the flask API
of the iReporter challenge.
---------------------------

"""

from app.views.views import UserAPI,IncidentAPI
from app import app

def user_api(view, pk='id', pk_type='int', **kwargs):
    view_func = view.as_view(kwargs['endpoint'])
    app.add_url_rule(kwargs['url'], defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(kwargs['url'], view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (kwargs['url'], pk_type, pk), view_func=view_func,
            methods=['GET', 'PATCH', 'DELETE'])

user_api(UserAPI, endpoint='user_api', url='/api/v1/users/', pk='id')

def incident_api(view, pk='id', pk_type='int', **kwargs):
    view_func = view.as_view(kwargs['endpoint'])
    app.add_url_rule(kwargs['url'], defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(kwargs['url'], view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (kwargs['url'], pk_type, pk), view_func=view_func,
            methods=['GET', 'PATCH', 'DELETE'])

incident_api(IncidentAPI, endpoint='incident_api', url='/api/v1/red-flags/', pk='id')

