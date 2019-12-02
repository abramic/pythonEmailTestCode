from flask import Flask, request, make_response, jsonify
app = Flask("python_email_test_server")

@app.route('/ping', methods = ['GET', 'PATCH', 'POST', 'PUT', 'DELETE'])
def handler():
    return make_response('Hello World From Python Test Email Server!', 200)

app.run(port=int('5001'), debug=True)
