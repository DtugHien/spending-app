from cmath import log
from datetime import datetime
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
import os

from sqlalchemy import null

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"

# Use a service account
# load_dotenv()
# key = {
#     "type": os.getenv("TYPE"),
#     "project_id": os.getenv("PROJECTID"),
#     "private_key_id": os.getenv("PRIVATE_KEY_ID"),
#     "private_key": os.getenv("PRIVATE_KEY").replace("\\n", '\n'),
#     "client_email": os.getenv("CLIENT_EMAIL"),
#     "client_id": os.getenv("CLIENT_ID"),
#     "auth_uri": os.getenv("AUTH_URI"),
#     "token_uri": os.getenv("TOKEN_URI"),
#     "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER"),
#     "client_x509_cert_url": os.getenv("CLIENT_CERT"),
# }
# cred = credentials.Certificate(key)

# firebase_admin.initialize_app(cred)

# db = firestore.client()

one_day_to_milisecond = 86400000
begin_date = int(datetime.strptime(
    datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d').timestamp() * 1000)
last_date = begin_date + one_day_to_milisecond
type_filter = "all"
types = {
    "buy": "Buy something",
    "game": "For game",
    "football": "For football",
    "other": "Other",
}


@app.route('/')
@cross_origin(origin='*')
def index():
    global type_filter, begin_date, last_date
    data = []
    # data = db.collection("spending").where(
    #     "time_stamp", ">=", begin_date).where("time_stamp", "<", last_date).stream()
    # data = [{**item.to_dict(), **{"id": item.id}} for item in data]
    # if (type_filter != "all"):
    #     data = [item for item in data if item['type'] == type_filter]
    total_price = sum([int(item['cost'].replace(",", ""))
                      for item in data])
    return render_template('index.html', render=data, types=types, total_price=f"{int(total_price):,}")


# @app.route('/add', methods=['POST'])
# @cross_origin(origin='*')
# def add():
#     data = request.get_json()
#     db.collection("spending").add({
#         "time_stamp": data['time_stamp'],
#         "spendOn": data['spendOn'],
#         "currency": data['currency'],
#         "type": data['type'],
#         "date": data['date'],
#         "cost": f"{int(data['cost']):,}",
#         "detail": data['detail'],
#     })
#     return jsonify(
#         {
#             "Status": "Ok",
#         }
#     )


# @app.route('/delete', methods=['DELETE'])
# @cross_origin(origin='*')
# def delete():
#     id = request.get_json()['id']
#     db.collection('spending').document(id).delete()
#     return jsonify(
#         {
#             "Status": "Ok"
#         }
#     )


# @app.route('/filter', methods=['UPDATE'])
# @cross_origin(origins='*')
# def add_filter():
#     global type_filter, begin_date, last_date
#     data = request.get_json()
#     type_filter = data['type']
#     if data["begin_time"] is None or data["last_time"] is None:
#         begin_date = int(datetime.strptime(
#             datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d').timestamp() * 1000)
#         last_date = begin_date + one_day_to_milisecond
#     else:
#         begin_date = data['begin_time']
#         last_date = data['last_time'] + one_day_to_milisecond
#     print(last_date, begin_date)
#     return "Filter"

port = int(os.environ.get("PORT", 5000))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
