import sys
import datetime
import functools
import os
import re
import urllib

from flask import (Flask, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *

ADMIN_PASSWORD = 'sarahisthebest'
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False
SECRET_KEY = 'shhh, secret!'
SITE_WIDTH = 800

app = Flask(__name__)
app.config.from_object(__name__)

flask_db = FlaskDB(app)
database = flask_db.database

oembed_providers = bootstrap_basic(OEmbedCache())


class Entry(Model):
    title = CharField()
    slug = CharField(unique=True)
    content = TextField()
    published = BooleanField(index=True)
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        database = database

    @property
    def html_content(self):
        hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
        extras = ExtraExtension()
        markdown_content = markdown(self.content, extensions=[hilite, extras])
        oembed_content = parse_html(
            markdown_content,
            oembed_providers,
            urlize_all=True,
            maxwidth=app.config['SITE_WIDTH'])
        return Markup(oembed_content)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = re.sub('[^\w]+', '-', self.title.lower())
        ret = super(Entry, self).save(*args, **kwargs)

        self.update_search_index()
        return ret

    def update_search_index(self):
        try:
            fts_entry = FTSEntry.get(FTSEntry.entry_id == self.id)
        except FTSEntry.DoesNotExist:
            fts_entry = FTSEntry(entry_id=self.id)
            force_insert = True
        else:
            force_insert = False
        fts_entry.content = '\n'.join((self.title, self.content))
        fts_entry.save(force_insert=force_insert)

    @classmethod
    def drafts(cls):
        return Entry.select().where(Entry.published == False)

    @classmethod
    def public(cls):
        return Entry.select().where(Entry.published == True)

    @classmethod
    def search(cls, query):
        words = [word.strip() for word in query.split() if word.strip()]
        if not words:
            # Return empty query.
            return Entry.select().where(Entry.id == 0)
        else:
            search = ' '.join(words)

        return (FTSEntry
                .select(
                    FTSEntry,
                    Entry,
                    FTSEntry.rank().alias('score'))
                .join(Entry, on=(FTSEntry.entry_id == Entry.id).alias('entry'))
                .where(
                    (Entry.published == True) &
                    (FTSEntry.match(search)))
                .order_by(SQL('score').desc()))


class FTSEntry(FTSModel):
    entry_id = IntegerField()
    content = TextField()

    class Meta:
        database = database


# def login_required(fn):
#     @functools.wraps(fn)
#     def inner(*args, **kwargs):
#         if session.get('logged_in'):
#             return fn(*args, **kwargs)
#         return redirect(url_for('login', next=request.path))
#     return inner


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     error = None
#     next_url = request.args.get('next') or request.form.get('next')
#     if request.method == 'POST' and request.form.get('password'):
#         password = request.form.get('password')
#         if password == app.config['ADMIN_PASSWORD']:
#             session['logged_in'] = True
#             session.permanent = True  # Use cookie to store session.
#             return redirect(next_url or url_for('index'))
#         else:
#             error = 'Incorrect password.'
#     return render_template('login.html', next_url=next_url, error=error)


# @app.route('/logout/', methods=['GET', 'POST'])
# def logout():
#     if request.method == 'POST':
#         session.clear()
#         return redirect(url_for('login'))
#     return render_template('logout.html')


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/Posts/')
def index():
    search_query = request.args.get('q')
    if search_query:
        query = Entry.search(search_query)
    else:
        query = Entry.public().order_by(Entry.timestamp.desc())
    return object_list('index.html', query, search=search_query,
                       check_bounds=False)


def _create_or_edit(entry, template):
    error = None
    if request.method == 'POST':
        entry.title = request.form.get('title') or ''
        entry.content = request.form.get('content') or ''
        entry.published = request.form.get('published') or False
        if not (entry.title and entry.content):
            error = 'Title and Content are required.'
        else:
            try:
                with database.atomic():
                    entry.save()
            except IntegrityError:
                error = 'Error: this title is already in use.'
            else:
                if entry.published:
                    return redirect(url_for('index', slug=entry.slug))
                else:
                    return redirect(url_for('drafts', slug=entry.slug))

    return render_template(template, entry=entry, error=error)


@app.route('/Create Entry/', methods=['GET', 'POST'])
# @login_required
def create():
    return _create_or_edit(Entry(title='', content=''), 'create.html')


@app.route('/Drafts/')
# @login_required
def drafts():
    query = Entry.drafts().order_by(Entry.timestamp.desc())
    return object_list('drafts.html', query, check_bounds=False)


@app.route('/<slug>/')
def detail(slug):
    if session.get('logged_in'):
        query = Entry.select()    
    else:
        query = Entry.public()
    entry = get_object_or_404(query, Entry.slug == slug)
    return render_template('detail.html', entry=entry)


@app.route('/<slug>/edit/', methods=['GET', 'POST'])
# @login_required
def edit(slug):
    entry = get_object_or_404(Entry, Entry.slug == slug)
    return _create_or_edit(entry, 'edit.html')


# @app.route('/about-me/')
# def about_me():
#     return render_template('about.html')


@app.template_filter('clean_querystring')
def clean_querystring(request_args, *keys_to_remove, **new_values):
    querystring = dict((key, value) for key, value in request_args.items())
    for key in keys_to_remove:
        querystring.pop(key, None)
    querystring.update(new_values)
    return urllib.urlencode(querystring)


@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Ruh roh, that page doesn\'t seem to exist!</h3>'), 404


def main():
    database.create_tables([Entry, FTSEntry], safe=True)
    app.run("0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
