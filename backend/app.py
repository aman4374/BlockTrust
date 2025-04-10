from flask import Flask, jsonify, Response
from flask_cors import CORS
from blockchain_simulation import run_simulation
import csv
import io

app = Flask(__name__)
CORS(app)

@app.route('/simulate', methods=['GET'])
def simulate():
    data = run_simulation()
    return jsonify(data)

@app.route('/download_csv', methods=['GET'])
def download_csv():
    data = run_simulation()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Round', 'Node ID', 'Action', 'Trust Score', 'Reputation', 'Stake', 'Penalty'])

    for round_num, round_data in enumerate(data, start=1):
        for node in round_data:
            writer.writerow([round_num, node['id'], node['action'], node['trust_score'], node['reputation'], node['stake'], node['penalty']])

    output.seek(0)
    return Response(output, mimetype='text/csv', headers={"Content-Disposition": "attachment; filename=simulation_results.csv"})

if __name__ == '__main__':
    app.run(debug=True)
