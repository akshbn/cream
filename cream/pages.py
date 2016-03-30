import os
from urllib.request import urlopen, Request
from .webconfig import theme,name

def getpage(pgn = None,plt = None):
    x = str(pgn)+".txt"
    with open(x,'w') as f:
        f.write("hello world!")

def check_in_assets(theme_name):
    path2assets = os.path.dirname(os.path.realpath(__file__)).split('/')
    css_files = os.listdir('/'.join(path2assets[:-1])+'/assets/css/')
    theme_file = theme_name + '.css'
    if theme_file in css_files:
        with open('/'.join(path2assets[:-1])+'/assets/css/'+theme_file,'r') as origin:
            contents = origin.read()
            return contents
    else:
        return get_bstrap_theme(theme_name)

def get_bstrap_theme(theme_name):
    user_agent = {'User-Agent': 'Firefox'}
    if theme_name == 'default':
        theme_url = 'https://bootswatch.com/bower_components/bootstrap/dist/css/bootstrap.min.css'
    else:
        theme_url = 'https://bootswatch.com/' + theme_name + '/bootstrap.min.css'
    # print(theme_url)
    download_req = Request(theme_url, data=None, headers=user_agent)
    t_file = urlopen(download_req)
    theme_content = t_file.read().decode('utf-8')
    path2assets = os.path.dirname(os.path.realpath(__file__)).split('/')
    path_to_theme = '/'.join(path2assets[:-1])+'/assets/css/'+theme_name+'.min.css'
    with open(path_to_theme,'w') as destination_file:
        destination_file.write(theme_content)
    return theme_content

def pageTemplate(name):
    path2assets = os.path.dirname(os.path.realpath(__file__)).split('/')
    cwd = os.getcwd()
    destination_folder = "%s/%s/" % (cwd,name)
    with open('/'.join(path2assets[:-1])+'/assets/config/cover.py','r') as origin:
        contents = origin.read()
        with open(cwd+'/'+name+"/coverMod.py",'w') as desti:
            desti.write(contents)
