import pymongo
from flask import Flask, jsonify, request, abort, json
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import date
import json
from bson import json_util, ObjectId

try:
    client = pymongo.MongoClient('mongodb://areixuser:<pw>@cluster0-shard-00-00.px1db.azure.mongodb.net:27017,cluster0-shard-00-01.px1db.azure.mongodb.net:27017,cluster0-shard-00-02.px1db.azure.mongodb.net:27017/expense?ssl=true&replicaSet=atlas-gd3kk5-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client['expense']
    collection = db['areix']

    # Retrieve the last record ID
    lastRecordId = collection.find().sort([('_id',-1)]).distinct('record_id')[-1] + 1
    print(lastRecordId)
# Catch DB errors
except Exception as e: 
    print(e)

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Backend-Testing"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/' )
def homePage():
    return "Hello, User!"


@app.route('/api/expense', methods=['GET', 'POST'])
def CreateExpense():
    
    if request.method == 'POST':

        global lastRecordId
        try:
            data = request.json
        except:
            abort(404)

        data["created_at"] = date.today().strftime("%Y-%m-%d")
        data["record_id"] = lastRecordId
       
        try:
            collection.insert_one(json.loads(json_util.dumps(data)))
            
        # Catch DB inserting errors    
        except Exception: 
            return jsonify(error="DB inserting errors"), 404

        out = {
            "data": data,
            "error": "false",
            "success": "true",
            "message": "Successfully Created A Record"
        }

        response = app.response_class(
        response=json.dumps(out),
        status=200,
        mimetype='application/json'
        )

        lastRecordId += 1

        return response

    return "/api/expense"
 
   

if __name__ == '__main__':
    app.run(debug=True)