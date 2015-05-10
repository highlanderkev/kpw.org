# coding: utf8
# database definitions for code snippets


# language enumerations for types of snippets
LANG_TYPE = ['Python','Java', 'HTML', 'CSS', 'JavaScript', 'Scala', 'Scheme']

# db definition for code snippet
db.define_table('snippet',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
				Field('description', 'string'),
                Field('langtype', requires=IS_IN_SET(LANG_TYPE)),
                Field('tags', 'list:string'),
				Field('body', 'text'))
db.snippet.id.readable = db.snippet.id.writable = False
