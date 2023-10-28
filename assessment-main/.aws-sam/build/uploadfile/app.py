import os
import json
import boto3
from flask_lambda import FlaskLambda
from flask import request, jsonify
import logging 



app1 = FlaskLambda(__name__)
BUCKET_NAME = os.environ.get('BUCKETNAME')
client = boto3.client('s3')

logger = logging.getLogger()
#print(TopicArnParameter.get("Parameter").get("Value"))


ALLOWED_EXTENSIONS = {'xlsm', 'xlsx', 'csv' }

# function to check file extension
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app1.route('/getdata', methods=['GET'])
def getFlightData():
    if request.method == 'GET':
        return json_response("test",200)
    else :
        return json_response("No data available",200)

@app1.route('/uploadfile', methods=['POST'])
def uploadFile():
    logging.info('POST  :::::: This is an info message')
    if request.method == 'POST':
        logging.info('POST  :: This is an info message')
        uploaded_file = request.files.get("file")
      
        logging.info('  BUCKET_NAME  :: '+BUCKET_NAME+"Filename  "+filename)
        if uploaded_file:
                filename = secure_filename(uploaded_file.filename)
                uploaded_file.save(filename)
                if file:
                    s3.upload_file(
                        Bucket = BUCKET_NAME,
                        Filename=filename,
                        Key = filename
                    )
                    msg = "Upload Done ! "
        return json_response(msg, 200)

def json_response(data, response_code):
    return json.dumps(data), response_code, {'Content-Type': 'application/json'}