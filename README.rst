===========
Cream
===========

**Cream is an experiment in scaffolding entire websites from templates.**

Need
=====

Most websites contain the same boilerplate of code . Hence it will be ideal to save time and effort
by using them by only modifying their contents. But, you will have to go through the
code and make modifications at all the required places. Later you have to check whether all aspects
of the website are working properly.

What if all you had to do was provide content and get a fully functional website in return?


Cream to the rescue!
========================

cream intends to do exactly that. It asks you for content to fill specific parts of the website
such as headings, navbar titles, footer etc and creates a fully functional website with it.


Installation
=============
1. Clone this repo into your computer ::

    git clone https://github.com/akshbn/cream

2. Navigate to the folder created by git ::

    cd cream/

3. Use ``setup.py`` to install cream ::

    python3 setup.py install

**Note:** ::

    Make sure you have setuptools installed on your machine as some
    environments dont come with it.

To install ``setuptools`` in Ubuntu, use ::

    sudo apt-get install python3-setuptools

cream will be installed and a script ``cream`` will be available for use.


Usage
======

Scaffolding a website involves 2 steps.

1. Creating the website config file and entering the contents
2. Using the config files to create a website

Config file
-----------------

1. Create the config files by typing ::

    cream website --theme <theme_name/default> <website_name>

2. A folder <website_name> will be created with config files for different pages of the website.

3. Each config file will contain prompts for content which are named after the elements of the site where the respective content will be inserted.

4. Fill in the content.

Create Website
---------------

1. ``cd`` into the folder containing the config files.

2. Use ``cream`` to create the website by using the following command ::

    cream generate

Cream will generate the website!

Contributing
=============

This an experiment and hence I am open to suggestions and feature requests. Open an issue for both.
For a feature request please include 'Feature' as part of the issue title.
For Suggestions/Feedback please include 'Feedback' as part of the issue title.
