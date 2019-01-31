import pandas as pd
import numpy as np
import json
from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route("/")
def home():
	return "hello world!"

@app.route("/df",methods=['GET'])
def ff():
	df = pd.read_csv("dataframe_post.csv")
	new_dict=df.to_dict("index")
	abc=list(new_dict.values())
	return json.dumps(abc)

@app.route("/add",methods=['POST'])
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

@app.route("/delete",methods=['DELETE'])
def del_data():
	data = request.get_json()
	df = pd.read_csv(r"dataframe_post.csv")
	# new_dict=df.to_dict("index")
	# list_of_df=list(new_dict.values())
	df = df[df['index'] != data['index']]
	df.to_csv(r'dataframe_post.csv',index = None, header=True)
	return jsonify({"index ":data["index"]})

@app.route("/update", methods=["PUT"])
def update_data():
	data = request.get_json()
	df = pd.read_csv(r"dataframe_post.csv")
	df.loc[df['index'] == data['index'],["nalme","roll_num","class"]] = data["name"],data["roll_num"],data["class"]
	df.to_csv(r'dataframe_post.csv',index = None, header=True)
	return jsonify({"index ":data["index"]})

if __name__ == "__main__":
    app.run(debug=True,port=4000)