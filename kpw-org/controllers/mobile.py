# coding: utf8
# mobile.py by Kevin Patrick Westropp

#########################################################################
## This is my main controller for the mobile website of kevinpatrickwestropp.org
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index(): 
    return dict(message="hello from mobile.py")
