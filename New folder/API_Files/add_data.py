import pandas as pd
import json
from flask import Flask,request,jsonify, Blueprint,redirect
app = Flask(__name__)

data_adding_app = Blueprint('data_adding_app', __name__)

@data_adding_app.route("/add",methods=['POST'])
def add_data():
	data = request.get_json()
	df = pd.read_csv("dataframe_post.csv")
	new_dict=df.to_dict("index")
	list_of_df=list(new_dict.values())
	created_df = {}
	created_df['index'] = (list_of_df[-1]['index']+1)
	combined_data = {**created_df,**data}
	df = df.append(combined_data,ignore_index = True)
	print(df)
	df.to_csv('dataframe_post.csv', index = None, header = True)
	return jsonify({"index ":created_df["index"]})
