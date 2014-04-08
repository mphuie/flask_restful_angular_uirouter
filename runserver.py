# app as application for wsgi
from myapp import app as application

application.run(debug=True, port=3000, host='0.0.0.0')