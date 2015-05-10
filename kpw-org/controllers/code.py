# coding: utf8
# code.py by Kevin Patrick Westropp

#########################################################################
## This is my controller for code snippets
## - index is the default action of any application
#########################################################################

import gluon.contrib.simplejson

# main overview of snippets
def index():
    response.flash = T('Navigate on the right to see the snippets on the left.')
    response.title = T('Code Snippets')
    files = db(db.snippet).select().as_list()
    return dict(files=gluon.contrib.simplejson.dumps(files))

# function to return code files
def snippets():
    files = ""
    if request.vars.values():
        files = request.vars.values()
    return dict(files=files)

def preview():
    snippet_id = request.args[0]
    filePreview = db(db.snippet.id==snippet_id).select().as_list()
    return dict(filePreview=filePreview)
