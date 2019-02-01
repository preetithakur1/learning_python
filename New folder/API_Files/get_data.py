import pandas as pd
import json
from flask import Flask,request,jsonify, Blueprint,redirect
app = Flask(__name__)

data_get_app = Blueprint('data_get_app', __name__)

@data_get_app.route("/get",methods=['GET'])
def ff():
	df = pd.read_csv("dataframe_post.csv")
	new_dict=df.to_dict("index")
	abc=list(new_dict.values())
	return json.dumps(abc)
