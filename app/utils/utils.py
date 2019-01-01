"""
Author: Allan Katongole
Date: 2nd January 2019
Utility methods for the application
including user access role management
---------------------------
"""

from functools import wraps
from flask import jsonify
from app.models.models import User

#user access role decorator for admin access
def requires_admin_access(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            admin_user = User.isAdmin
            if admin_user == False:
                return jsonify({"status":401, "error":"You dont have access to this endpoint"}) 
            return f(*args, **kwargs)
        return decorated_function
    return decorator