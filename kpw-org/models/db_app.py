# coding: utf8
# database definition for my app
# By Kevin Westropp

import datetime

#MY FUNCTIONS

# method to format datetime
def get_dateday(datetimeobject):
    datestring = datetimeobject.strftime("%b %d, %Y")
    return datestring

# basic email db definition
db.define_table('email',
                Field('send_to', 'string', requires=IS_EMAIL()),
                Field('sent_by', 'string', requires=IS_EMAIL()),
                Field('subject', 'string'),
                Field('body', 'text', requires=IS_NOT_EMPTY()))
