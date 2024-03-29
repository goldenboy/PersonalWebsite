# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
POST_SHOW_COUNT = 5

def index():
    response.files.append(URL(request.application, 'static/css', 'index.css'))
    # Return the most recent X posts to display on the page.
    allPosts = db().select(db.posts.ALL, orderby =~ db.posts.date)
    recentPosts = allPosts[:POST_SHOW_COUNT]
    return dict(posts = recentPosts)

def about():
    response.files.append(URL(request.application, 'static/css', 'about.css'))
    return dict()

def resume():
    response.files.append(URL(request.application, 'static/css', 'resume.css'))
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_membership('SuperUser')
def edit_post():
    """ Allows for editing of the selected post. Post id passed as a query
    parameter. 
    """
    post_id = request.vars['post']
    update_form = crud.update(db.posts, post_id, next=URL('index'))
    return dict(form=update_form)

@auth.requires_membership('SuperUser')
def data():
    """                                      
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs bust be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

@auth.requires_membership('SuperUser')
def create_post():
    """ Write a new blog post. """
    makePost = crud.create(db.posts, next=URL('index'))
    return dict(form=makePost)
