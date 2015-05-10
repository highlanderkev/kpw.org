# coding: utf8
# database definitions for Resume/CV

import datetime

#functions

# method to format datetime (month, year)
def get_datemonthyear(datetimeobject):
    if(isinstance(datetimeobject, datetime.datetime)):
        datestring = datetimeobject.strftime("%b, %Y")
    else:
        datestring = "Present"
    return datestring


# db definition for degree
db.define_table('diploma',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('university', 'string'),
                Field('website', 'string'),
                Field('geolocation', 'string'),
                Field('datefrom', 'datetime'),
                Field('dateto', 'datetime'),
                Field('ongoing', 'boolean'),
                Field('studyfocus', 'string'),
                Field('honors', 'list:string'),
                Field('extra', 'list:string'))
db.diploma.id.readable = db.diploma.id.writable = False


# db definition for course
db.define_table('course',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('description', 'text'),
                Field('website', 'string'),
                Field('tags', 'list:string'),
                Field('course_id', 'string'))
db.course.id.readable = db.course.id.writable = False

# db definition for professional experience
db.define_table('professional_experience',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('company', 'string'),
                Field('website', 'string'),
                Field('geo_location', 'string'),
                Field('datefrom', 'datetime'),
                Field('dateto', 'datetime'),
                Field('present', 'boolean'),
                Field('tasks', 'list:string'),
                Field('intern', 'boolean'))
db.professional_experience.id.readable = db.professional_experience.id.writable = False

# db definition for volunteer experience
db.define_table('volunteer_experience',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('company', 'string'),
                Field('website', 'string'),
                Field('geo_location', 'string'),
                Field('datefrom', 'datetime'),
                Field('dateto', 'datetime'),
                Field('present', 'boolean'),
                Field('tasks', 'list:string'))
db.volunteer_experience.id.readable = db.volunteer_experience.id.writable = False

TECH_TYPE = ['Multi-paradigm Programming', 'Imperative Programming', 'Object-oriented Programming', 'Functional Programming', 'Database Development', 'Web Development', 'Web Frameworks', 'Data Markup', 'Mobile Development', 'Statistical Programming', 'Systems', 'System Tools', 'Build Tools']

# db definition for technical experience
db.define_table('technical_experience',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('tech_type', requires=IS_IN_SET(TECH_TYPE)),
                Field('website', 'string'),
                Field('my_background', 'string'))
db.technical_experience.id.readable = db.technical_experience.id.writable = False

COMM_TYPE = ['Language', 'Rhetoric', 'Design']

# db definition for Communication experience
db.define_table('communication_experience',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('comm_type', requires=IS_IN_SET(COMM_TYPE)),
                Field('my_background', 'string'))
db.communication_experience.id.readable = db.communication_experience.id.writable = False


# db definition for interests
db.define_table('interest',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('body', 'text'))
db.interest.id.readable = db.interest.id.writable = False

# db definition for organizations
db.define_table('organization',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('website', 'string'),
                Field('overview', 'text'))
db.interest.id.readable = db.interest.id.writable = False
