import os
from .pages import get_bstrap_theme

def getassets():
    '''
    Currently fetches bootstrap themes from bootswatch.com

    Additional sources will be added in time.
    '''
    bootstrap_themes = ['default','cerulean','cosmo','cyborg','darkly','flatly','journal','lumen','paper','readable','sandstone','simplex','slate','spacelab','superhero','united','yeti']
    for theme in bootstrap_themes:
        print("Downloading %s..." % theme)
        get_bstrap_theme(theme)
        print("Completed")
