# coding: utf8
# database definitions for post/blog

import urllib

# method to get post content from main webpage
def get_postcontent(link):
    page = urllib.urlopen(link).read()
    start = page.find('<section>')
    end = page.find('</section>')
    page = page[start:end]
    return page

# db definition for posts
db.define_table('post',
                Field('title', 'string', requires=IS_NOT_EMPTY()),
				Field('subtitle', 'string'),
                Field('date_posted', 'datetime'),
                Field('date_updated','datetime'),
                Field('tags', 'list:string'),
				Field('body', 'text'),
				Field('description', 'string'))
db.post.id.readable = db.post.id.writable = False
