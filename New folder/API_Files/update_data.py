import pandas as pd
import json
from flask import Flask,request,jsonify, Blueprint,redirect
app = Flask(__name__)

data_update_app = Blueprint('data_update_app', __name__)

@data_update_app.route("/update", methods=["PUT"])
def update_data():
	data = request.get_json()
	df = pd.read_csv(r"dataframe_post.csv")
	df.loc[df['index'] == data['index'],["name","roll_num","class"]] = data["name"],data["roll_num"],data["class"]
	df.to_csv(r'dataframe_post.csv',index = None, header=True)
	return jsonify({"index ":data["index"]})