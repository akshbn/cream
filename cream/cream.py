import sys
import argparse
from .pages import getpage
from .fetch import getassets
from .webs import createWebs,generateWebs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch",action='store_const',const='all',help = "fetch all bootstrap themes from bootswatch.com")
    parser.add_argument("-v","--version",action='store_const',const='all',help="Displays the version number")
    subcommand = parser.add_subparsers(dest = 'cmd_name')

    #all sub commands which can be used
    page = subcommand.add_parser('page',help = "scaffold a page")
    page.add_argument("pgname",help = "page name")
    page.add_argument("-lyt","--layout", help = "the type of html page. Eg: Login,cover etc")

    website = subcommand.add_parser('website',help = "Scaffold a complete Website")
    website.add_argument("website_name",help = "The website name")
    website.add_argument("--theme",help = "bootstrap theme to use",required = True)

    gen = subcommand.add_parser('generate',help = "generate the static files")
    gen.add_argument("--dest",help="path to the destination folder")

    args = parser.parse_args()
    if args.fetch:
        getassets()
        return
    if args.version:
        ver = __import__('cream').__version__
        print(ver)
        return
    if args.cmd_name == "page":
        if args.layout:
            getpage(pgn = args.pgname,pth = args.layout)
        else:
            getpage(pgn = args.pgname)
    elif args.cmd_name == "generate":
        from os import getcwd
        if args.dest:
            current_path = args.dest
            print(current_path)
            print(type(current_path))
        else:
            current_path = getcwd()
        generateWebs(current_path)
    elif args.cmd_name == "website":
        createWebs(args.website_name,args.theme)


# if __name__ == '__main__':
#     main()
