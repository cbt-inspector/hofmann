Main script for the website of Joachim Hofmann

Functions in files:

- main.py:
    - routing of requests via flask
    - returning HTML files with jinja2 arguments
    - serving these files to the user

- requirements.txt:
    - text file for all required Python modules for easy installation

- app.ini:
    - Init file for an uwsgi server (with arguments)

- templates folder:

    - base.html:
        - base template for the webpage

    - index.html:
        - the main page including building up the list of directories

    - dir.html:
        - template for building up the list of directory contents
        - navigation buttons, current location listing

- static folder:

    - css folder:
        - base.js:
            - Base Styles used all over the page.
        - about.css:
            - Styles for the 'about.html' template page.
        - datenschutz.css:
            - Styles for the 'datenschutz.html' template page.
        - dir.css:
            - Styles for the 'about.html' template page.
        - error.css:
            - Styles for the Error page.

    - js folder:
        - base.js:
            - Main JavaScript functions for the page.

    - assets folder:
        - Icons used on the pages
        - Backgrounds for pages

    - files folder:
        - All files to be served as content on the page


Setup:
- install all required dependencies via
$ pip install -r requirements.txt


- This script is meant to be running on an uWSGI server, preferrably behind nginx.
    Quickstart docs: https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
    nginx docs: https://www.nginx.com/resources/wiki/start/topics/tutorials/install/


- Paste into the nginx config file (/etc/nginx/sites-enabled/YOUR_SITE.conf):

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:3031;
    }

- Now add uwsgi to the services started at boot (Ubuntu uses Systemd, so the docs are at https://uwsgi-docs.readthedocs.io/en/latest/Systemd.html)

- Use certbot to get a free Let'sEncrypt SSL certificate
    Docs: https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal
    - Certbot automatically refreshes the certificate when it expires.


Testing the website locally:
- install all required dependencies via
$ pip install -r requirements.txt

- Testing after this step is easy, just run this python script and open up http://127.0.0.1:5000 in your browser.


