from flask import Flask, render_template
from query_db import select as my_select

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");
@app.route('/data_api')
def dat_api():
    contact = my_select()
    return contact
@app.route('/movie')
def view():
    contact = my_select()
    return render_template("movie.html", contact=contact);
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)
