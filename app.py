from Scanner.scanner import search as arxsearch

from flask import Flask, redirect, url_for, request, render_template,Response,json
from werkzeug.utils import secure_filename

from datetime import timedelta

# Define a flask app
app = Flask(__name__)
app.config['DEBUG']=False
app.config['SEND_FILE_MAX_AGE_DEFAULT']=timedelta(seconds=1)

newContent=None
topic=None
@app.route('/', methods=['GET'])
@app.route('/search', methods=['GET'])
def search():
    # Main page
    return render_template('search.html')


@app.route('/searchContent', methods=['GET', 'POST'])
def searchContent():
    if request.method == 'POST':
        f = request.get_json()
        searchcontent=f['content']
        searchresult=arxsearch(searchcontent,100)
        return Response(json.dumps(searchresult), mimetype='application/json')
    return "pass"





if __name__ == '__main__':

    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.run()


    # Serve the app with gevent
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
