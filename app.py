import os
import sys
import flask

import clusters
import settings


#sys.path.insert(0, os.getcwd())
app = flask.Flask(__name__)
if settings.FLASK_SETTINGS is not None:
    app.config.update(settings.FLASK_SETTINGS)
    

@app.route('/')
def index():
    urls = ['https://tphan.cloudant.com/test-cluster/_design/multitenant/_view/version?group=true',
           'https://tphan.cloudant.com/test-cluster/_design/dedicated/_view/version?group=true',
           'https://tphan.cloudant.com/test-cluster/_design/bluemix/_view/version?group=true']
    myclusters = {
        "Multi-Tenant": [],
        "Dedicated": [],
        "Bluemix": []
    }
    for url in urls:
        clusters_json = clusters.get_clusters(url)
        for c in clusters_json:
            if (url.find("multitenant") != -1 ):
                myclusters["Multi-Tenant"].append(c) 
            elif (url.find("dedicated") != -1):
                myclusters["Dedicated"].append(c)
            elif (url.find("bluemix") != -1):
                myclusters["Bluemix"].append(c)
                
    return flask.render_template('index.html',
        clusters=myclusters
    )
    
@app.errorhandler(404)
def not_found(error):
    return flask.render_template('error.html'), 404

if __name__ == '__main__':
    print "test it: "
    app.debug = True
    app.run()
