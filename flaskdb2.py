# -------------------------------------------------------------------------- 
# This is asimple service examples that returns json array of arrays of data
# Objects is not created for simplicity reasons 
# Niels Liisberg 2019.11.01, System & Method - Project Sitemule
# -------------------------------------------------------------------------- 
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import jsonify
import ibm_db_dbi as db

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

#conn = db.pconnect (dsn=None, user='demo', password='demo' , database='*LOCAL',conn_options=None)
conn = db.pconnect (database='*LOCAL')


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# http://dksrv131:5000/list_users_by_proc
@app.route('/list_users_by_proc')
def list_users_by_proc():

	cur = conn.cursor()
	cur.callproc ('microdemo.user_list', ['sen'])
	rows  = cur.fetchall()
	cur.close()
	return jsonify(rows)


# http://dksrv131:5000/list_users_by_view
@app.route('/list_users_by_view')
def list_users_by_view():

	cur = conn.cursor()
	cur.execute('select * from microdemo.users_full')
	rows  = cur.fetchall()
	cur.close()
	return jsonify(rows)


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	# the host='0.0.0.0' describes the interface - aka. "any"  interface
	app.run(host='0.0.0.0')


