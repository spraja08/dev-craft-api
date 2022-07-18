from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import json


app = Flask("Dev-Craft-API")
CORS(app)
api = Api(app)

metadata = {}
entries = os.listdir('./docs')
for entry in entries:
    with open('./docs/' + entry, 'r') as f:
        print(entry[:-3])
        metadata[entry[:-3]] = f.read()

class DevCraftAPI(Resource):
    def get(self):
        return metadata
    
    def get(self, id):
        returnval  = {}
        returnval["result"] = metadata[id]
        return json.dumps(returnval)
        #return metadata[id]

api.add_resource(DevCraftAPI, '/metadata/<id>')

if( __name__ == '__main__'):
    app.run()