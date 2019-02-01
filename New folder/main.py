from flask import Flask, Blueprint, request,jsonify,redirect

from API_Files.add_data import data_adding_app
from API_Files.delete_data import data_delete_app
from API_Files.update_data import data_update_app
from API_Files.get_data import data_get_app

app = Flask(__name__)

app.register_blueprint(data_adding_app)
app.register_blueprint(data_delete_app)
app.register_blueprint(data_update_app)
app.register_blueprint(data_get_app)

@app.route('/')
def welcome():
	return "Welcome To The World Of APIs"	

if __name__ == '__main__':
	app.run(port=3330,debug = True)

