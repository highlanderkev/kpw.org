# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(IMG(_src=URL('static', 'images/kpw.png'), _alt="KPW Logo", _height="25", _width="25"),
                  _class="brand", _href="http://www.kevinpatrickwestropp.org/")
response.title = 'KPW'
response.subtitle = get_dateday(request.now)

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Kevin Patrick Westropp <mail@kevinpatrickwestropp.com>'
response.meta.description = 'Kevin Patrick Westropp - projects, development and computer science stuff.'
response.meta.keywords = 'programmimng, development, graduate, computer, science'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = 'UA-44734346-1'

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Projects'), False, URL('projects', 'index'), []),
    (T('Blog'), False, URL('blog', 'index'), []),
    (T('Code Snippets'), False, URL('code', 'index'), []),
]

response.menu_right = [
                       (XML('R&#233sum&#233/CV'), False, URL('cv', 'index'), []),
                       ]
