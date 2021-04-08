# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import click
from flask import Blueprint
from flask import current_app

import re

commands = Blueprint('commands', __name__)

@commands.cli.command('hello')
def hello():
    """ Simple Hello """
    print("Custom command - Hello")

@commands.cli.command('cfg')
@click.argument('filter', required=False)
def config(filter=None):
    """ List all Config Variables """
    print("Custom command - Cfg(Filter="+str(filter)+")")
    for key in current_app.config:

        val = str( current_app.config[key] )

        # Filtered config
        if filter:    
            if re.search(filter, key, re.IGNORECASE):
                print (  '  |- ' + key  + ' -> ' + val )

        # Unfiltered config
        else:
            print (  '  |- ' + key  + ' -> ' + val )
