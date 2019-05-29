###################################################################################
#	Flask Website / 0.0
#	kemotep
#	2019-05-28 / GNU Affero General Public License v3
#	kemotep@gmail.com / https://github.com/kemotep/
###################################################################################
import datetime
import functools
import os
import re
import urllib
import config
from flask import (Flask, flash, Markup, redirect, render_template, request,
                   Response, session, url_for)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *
from bcrypt import hashpw, gensalt, checkpw
from flask_sslify import SSLify

### WORK IN PROGRESS ###
### REMEMBER TO CREATE NOTES FOR VIRTUAL ENV ###