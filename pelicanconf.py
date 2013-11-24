#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'João Faria'
SITENAME = u'Homepage'
SITEURL = 'https://www.astro.up.pt/~jfaria/'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'css', 'js']


# Specify name of a built-in theme
#THEME = "simple"
# Other themes
THEME = "simple_personal"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
