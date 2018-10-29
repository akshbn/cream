import os

def asset_path():
    '''
    Returns the assets folder path.
    '''
    if os.name == 'nt': #In windows '\' is used as a directory separator.
        folder_separator = '\\'
    else:
        folder_separator = '/'
    cream_dir = os.path.dirname(os.path.realpath(__file__)).split(folder_separator)
    asset_dir = cream_dir[:-1]
    asset_dir.append('assets')
    asset_dir_path = folder_separator.join(asset_dir)
    return asset_dir_path

def convert_to_linuxpath(win_path):
    '''
    Converts a windows file path to a linux file path.
    ''' 
    temp = win_path.split('\\')
    return '/'.join(temp)
