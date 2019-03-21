from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

uri = "localhost:27017"
client = MongoClient(uri)

mongo_db = client["mydb"]

frameworks_db = mongo_db.frameworks

@app.route('/framework', methods = ['GET'])
def get_all_frameworks():
	# get all the frameworks....
	output = []

	for query in frameworks_db.find():
		# fetch the framework data...
		output.append({"name" : query['name'], "language" : query['language']})

	print "All the frameworks are queried from frameworks collection..."

	#print output, "#######"

	return jsonify({'result' : output})

@app.route('/framework/<name>', methods = ['GET'])
def get_one_framework(name):
	# get one framework....
	result = frameworks_db.find_one({"name" : name})

	if result:
		output = {'name' : result['name'], 'language' : result['language']}
	else:
		output = 'No results found'

	return jsonify({'result' : output})

@app.route('/framework', methods = ['POST'])
def add_one_framework():
	# request parameters....
	name = request.json['name']
	language = request.json['language']

	# insertion of data into the frameworks collection.....
	framework_id = frameworks_db.insert({'name' : name, 'language' : language})

	new_framework = frameworks_db.find_one({'_id' : framework_id})

	output = {'name' : new_framework['name'], 'language' : new_framework['language']}

	return jsonify({'result' : output})


if __name__ == "__main__":
	app.run(debug=True)
