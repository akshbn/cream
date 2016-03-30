import os
from .pages import get_bstrap_theme

def getassets():
    '''
    Used to fetch bootstrap themes'''
    bootstrap_themes = ['default','cerulean','cosmo','cyborg','darkly','flatly','journal','lumen','paper','readable','sandstone','simplex','slate','spacelab','superhero','united','yeti']
    for theme in bootstrap_themes:
        print("Downloading %s..." % theme)
        get_bstrap_theme(theme)
        print("Completed")
