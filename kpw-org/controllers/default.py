# -*- coding: utf-8 -*-
# default.py by Kevin Patrick Westropp

#########################################################################
## This is my main controller for kevinpatrickwestropp.org
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

#if request.user_agent().is_mobile:
response.view.replace('.html','.mobile.html')

#Mobile Views
from gluon.contrib.user_agent_parser import mobilize

# method for default loading page
@mobilize
def index():
    response.flash = T("Welcome to KPW.org!")
    response.title = T('KPW.org')
    message = ""
    return dict(message=message)

# method to show twitter feed
def twitterfeed():
    return dict()

# method for user logins and registration (currently disabled)
'''
def user():
    return dict(form=auth())
'''

# method for downloading files (currently disabled)
'''
@cache.action()
def download():
    return response.download(request, db)
'''
# decorate with @services.jsonrpc the functions to expose
# supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
def call():
    return service()

# method for SQL table manipulation (currently disabled)
'''
@auth.requires_signature()
def data():
    return dict(form=crud())
'''
