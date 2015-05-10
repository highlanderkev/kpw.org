# -*- coding: utf-8 -*-
# cv.py by Kevin Patrick Westropp

#########################################################################
## This is my controller for kevinpatrickwestropp.org/cv
#########################################################################


def index():
    response.flash = T('Welcome to my resume/cv.')
    response.title = T('KPW CV')
    #projects = db(db.project).select()
    projects = ''
    posts = ''
    courses = db(db.course).select(orderby=db.course.title)
    jobs = db(db.professional_experience.intern == False).select(orderby=~db.professional_experience.datefrom)
    internships = db(db.professional_experience.intern == True).select(orderby=~db.professional_experience.datefrom)
    volunteering = db(db.volunteer_experience).select(orderby=~db.volunteer_experience.datefrom)
    organizations = db(db.organization).select()
    diplomas = db(db.diploma).select(orderby=~db.diploma.datefrom)
    technical = {}
    for tech in TECH_TYPE:
        technical[tech] = db(db.technical_experience.tech_type==tech).select()
    communications = {}
    for comm in COMM_TYPE:
        communications[comm] = db(db.communication_experience.comm_type==comm).select()
    return dict(projects=projects,posts=posts,courses=courses,jobs=jobs,internships=internships,volunteering=volunteering,technical=technical,communications=communications,organizations=organizations,diplomas=diplomas)
