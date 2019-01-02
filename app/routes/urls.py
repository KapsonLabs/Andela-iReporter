"""
Author: Allan Katongole
Date: 28th December 2018
Routes for the flask API
of the iReporter challenge.
---------------------------

"""

from app.views.views import UserAPI,IncidentAPI
from app import app

def user_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
            methods=['GET', 'PATCH', 'DELETE'])

user_api(UserAPI, 'user_api', '/api/v1/users/', pk='id')

def incident_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
            methods=['GET', 'PATCH', 'DELETE'])

incident_api(IncidentAPI, 'incident_api', '/api/v1/red-flags/', pk='id')

