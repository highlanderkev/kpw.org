# coding: utf8
# database definition for my projects
# By Kevin Westropp


# db definition for project
db.define_table('project',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('date_created', 'datetime'),
                Field('description', 'text'),
                Field('readme','text'),
                Field('link', 'string'),
                Field('code', 'string'),
                Field('tags', 'list:string'),
                Field('is_active','boolean'))
db.project.id.readable = db.project.id.writable = False

# db definition for web2py example project
db.define_table('example',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('date_created', 'datetime'),
                Field('description', 'text'),
                Field('link', 'string'),
                Field('code', 'string'),
                Field('downloadable', 'string'),
                Field('blogpost','string'),
                Field('tags', 'list:string'),
                Field('icon', 'string'))
db.example.id.readable = db.example.id.writable = False
