import os
from .pages import pageTemplate

def createWebs(names,themes):
    cwd = os.getcwd()
    os.makedirs(names)
    files = "%s/%s" % (names,names+"Config.py")
    with open(os.path.dirname(os.path.realpath(__file__))+'/webconfig.py','r') as origin:
        contents = origin.read()
        from string import Template
        subs = Template(contents)
        renderedTemplate = subs.substitute(name = names,theme = themes)
        with open(files,'w') as dest:
            dest.write(renderedTemplate)
    layouts = ['cover']
    pageTemplate(names,layouts)

def generateWebs(path):
    from os import listdir,chdir
    file_list = listdir(path)
    print(file_list)
    is_present = 0
    import re
    fpattern = re.compile('((\w+)Config)\.py$')
    chdir(path)
    for file in file_list:
        extractor = fpattern.match(file)
        if extractor != None:
            folder_name = extractor.group(2)
            file_name = extractor.group(2)+'.'+extractor.group(1)
            print(file_name)
            is_present = 1
            from importlib import import_module
            config = import_module(file_name)
            module_list = dir(config)
            print("module list = ",module_list)
            module_pattern = re.compile('(\w+Mod)$')
            for module in module_list:
                ext_module = module_pattern.match(module)
                if ext_module != None:
                    mod_name = folder_name+'.'+ext_module.group(1)
                    module_imp = import_module(mod_name)
                    render(module_imp,config)
    if is_present == 0:
        print("Cream couldn't find any Config file in this directory. Cd to your Config directory created using website command")

def render(module_imp,config_fi):
    print(module_imp)
    if module_imp.mod_type is "cover":
        with open('../../assets/html/CoverPage.html','r') as origin:
            content = origin.read()
            from string import Template
            from .helper_functions import asset_path
            asset_dir = asset_path()
            bootstrapcss = asset_dir + '/css/bootstrap.min.css'
            bootstrapjs = asset_dir + '/js/bootstrap.min.js'
            covercss = asset_dir + '/css/CoverPage.css'
            temp = Template(content)
            tst = temp.substitute(brand = config_fi.name,nav1 = module_imp.nav1,nav2 = module_imp.nav2,nav3 = module_imp.nav3,heading = module_imp.headline,text = module_imp.text,bootstrapCss=bootstrapcss,\
            bootstrapJs=bootstrapjs,pageCss=covercss)
            with open('edited.html','w') as desti:
                desti.write(tst)
            # with open('CoverTemp/cover.css','r') as origin:
            #     content = origin.read()
            #     from string import Template
            #     temp = Template(content)
            #     csstr = temp.substitute(bimg = module_imp.background_image)
            #     with open('edited.css','w') as desti:
            #         desti.write(csstr)
