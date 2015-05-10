# coding: utf8
# blog.py by Kevin Patrick Westropp

#########################################################################
## This is my controller for kevinpatrickwestropp.org/blog
#########################################################################

# main page for blog
def index():
    response.title = T('Blog')
    posts = db(db.post).select(orderby=~db.post.date_posted)
    return dict(posts=posts)

#method to show post
def post():
    post = db.post(request.args(0,cast=int)) or redirect(URL('blog','index'))
    postcontent = post.body
    response.title = post.title
    response.subtitle = post.date_posted
    return dict(postcontent=postcontent, post=post)

# method to show a list/table of all posts
def postlist():
    posts = db(db.post).select(orderby=~db.post.date_posted)
    return dict(posts=posts)

# method to show a list/table of all posts
def postlistmedia():
    posts = db(db.post).select(orderby=~db.post.date_posted)
    return dict(posts=posts)
