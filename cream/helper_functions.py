import os

def asset_path():
    if os.name == 'nt':
        folder_separator = '\\'
    else:
        folder_separator = '/'
    cream_dir = os.path.dirname(os.path.realpath(__file__)).split(folder_separator)
    asset_dir = cream_dir[:-1]
    asset_dir.append('assets')
    asset_dir_path = folder_separator.join(asset_dir)
    return asset_dir_path
