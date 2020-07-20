import click
from flask.cli import with_appcontext

from NewsFeed import db
from NewsFeed.models import User, Post

@click.command(names='create_tables')
@with_appcontext
def create_tables():
	db.create_all()