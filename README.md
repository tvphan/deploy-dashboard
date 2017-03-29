DBCore Deployment Dashboard
=======

This dashboard gives the overview of how many builds deployed on production clusters.
Clusters to be included are: Multi Tenant, Dedicated, and Bluemix.

This dashboard is using as FLASK app to run with cluster daemon in Python, and the frontend purely html5 and JavaScript.
Flask app is python based and embedded Jinja2 template (as language to communicate with HTML on the frontend)

Info for Flask and Jinja2:
http://flask.pocoo.org/docs/0.12/quickstart
http://jinja.pocoo.org/docs/2.9/templates/


Running locally
---------------

You may need to install `virtualenv` if you haven't already. Check your
package manager or try `sudo easy_install virtualenv`.

    $ clone the repo from Cloudant github, "https://github.com/cloudant/dbcore-deployment-dashboard"
    $ cd dbcore-deployment-dashboard
    $ virtualenv --no-site-packages venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ vim local_settings.py

    # Here's what local_settings.py should look like:

    ADMIN = ("adm", "password")
    FLASK_SETTINGS = { 'DEBUG' : True, 'TESTING' : False}                                                                                            
    # Running it locally on your laptop for development purpose
    1. Create a pydev project in Eclipse and run the app there OR
    2. Run on cmd line option, cmd line option to run at the level of app.py
       $ python -m flask run 

    # Flask app run individually has a limitation of handle multiple requests, it could cause local server crash if heavy loads
    # The recommendation is to deploy it as single container on virtualenv
    # Options can be Green Unicorn, or self host with Apache
    # More info on this: http://flask.pocoo.org/docs/0.12/deploying/#deployment

    # How to run the app in a single container - <<< under construction for testing stability >>>

      
 
    # When you're done you'll want to exit your virtualenv
    # before working on any other Python projects
    $ deactivate
