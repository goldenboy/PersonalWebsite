# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.title = 'Greg Bigelow'
response.meta.author = 'Greg Bigelow'
response.meta.description = 'The personal website of Greg Bigelow.'
response.meta.keywords = 'Greg Bigelow'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [('Home', True, URL('index'), []), ('About', False, URL('about'), []),
        ('Resume', False, URL('resume'), [])] 
