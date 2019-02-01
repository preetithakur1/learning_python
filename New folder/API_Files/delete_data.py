import pandas as pd
import json
from flask import Flask,request,jsonify, Blueprint,redirect
app = Flask(__name__)

data_delete_app = Blueprint('data_delete_app', __name__)

@data_delete_app.route("/delete",methods=['DELETE'])

def del_data():
	data = request.get_json()
	df = pd.read_csv(r"dataframe_post.csv")
	# new_dict=df.to_dict("index")
	# list_of_df=list(new_dict.values())
	df = df[df['index'] != data['index']]
	df.to_csv(r'dataframe_post.csv',index = None, header=True)
	return jsonify({"index ":data["index"]})
