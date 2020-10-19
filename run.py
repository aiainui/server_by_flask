from app import app
from gevent.pywsgi import WSGIServer
import setting
if __name__ == "__main__":
    app.debug = setting.DEBUG
    WSGIServer(('0.0.0.0',setting.FlaskSettings.PORT), app).serve_forever()