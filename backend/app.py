from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from classes.Report import Report

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
report = Report()

@app.route('/create_report', methods=['GET'])
@cross_origin()
def create_report():
    suspect_name = request.args.get('suspect_name')
    dept = request.args.get('dept')
    action_category = request.args.get('action_category')
    description = request.args.get('description')
    location = request.args.get('location')
    time_of_occurence = request.args.get('time_of_occurence')
    evidence = request.args.get('evidence')

    previous_block = report.print_previous_block()
    previous_proof = previous_block['proof']
    proof = report.proof_of_work(previous_proof)
    previous_hash = report.hash(previous_block)
    block = report.create_block(proof, previous_hash, suspect_name, dept, action_category, description, location, time_of_occurence, evidence)

    response = {'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'suspect_name': block['suspect_name'],
                'dept': block['dept'],
                'action_category': block['action_category'],
                'description': block['description'],
                # optional fields
                'location': block['location'],
                'time_of_occurence': block['time_of_occurence'],
                # evidence as string, divide by comma and convert to list
                'evidence': [block['evidence'].split(',')]}

    return jsonify(response), 200

@app.route('/reports', methods=['GET'])
@cross_origin()
def display_reports():
    response = {'chain': report.chain[1:],
                'length': len(report.chain)-1}
    return jsonify(response), 200

@app.route('/reports/<int:index>', methods=['GET'])
@cross_origin()
def display_report_by_id(index):
    for block in report.chain:
        if block['index'] == index:
            response = {'block': block}
            return jsonify(response), 200
    response = {'message': 'Block not found!'}
    return jsonify(response), 404

@app.route('/valid', methods=['GET'])
def valid():
    valid = report.chain_valid(report.chain)

    if valid:
        response = {'message': 'The system is valid.'}
    else:
        response = {'message': 'The system is not valid.'}
    return jsonify(response), 200

# Run the flask server locally
app.run(host='127.0.0.1', port=5000)