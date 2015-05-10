# coding: utf8
# projects.py by Kevin Patrick Westropp

#########################################################################
## This is my controller for kevinpatrickwestropp.org/projects
#########################################################################

# main page for Projects
def index():
    response.title = T('Projects')
    projects = db(db.project).select()
    return dict(projects=projects)

# method to preview the project
def project_preview():
    project = db.project(request.args(0,cast=int))
    return dict(project=project)

# method to see a list of all projects
def projectlist():
    projects = db(db.project).select()
    return dict(projects=projects)

# method to see the projects in groups of divs (3 per row)
def projectgroup():
    projects = db(db.project).select()
    return dict(projects=projects)

#method to show web2py examples
def web2pyexamples():
    examples = db(db.example).select()
    return dict(examples=examples)
