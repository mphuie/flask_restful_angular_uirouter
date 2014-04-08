from myapp import app
from flask import render_template

@app.route("/")
def home():
  return app.send_static_file('index.html')