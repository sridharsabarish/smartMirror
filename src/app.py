from flask import Flask, render_template_string
from smartMirror import smartMirror

import datetime
import csv
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def serve_page():
    smartmirror = smartMirror()
    html = smartmirror.build_web_page()
    return render_template_string(html)


@app.route('/meal', methods=['GET'])
def get_meal_plan():

    with open('meal_plan.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    result = {}
    for row in rows:
        key = row[list(rows[0].keys())[0]]
        result[key] = {field: row[field] for field in list(rows[0].keys())[1:]}

    print(result)


    today = datetime.date.today().strftime("%A")
    result = {today: result[today]} if today in result else {}
    return jsonify(result[today])
    # return json.dumps(result, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)