from flask import Flask, jsonify, request, make_response
import flask_cors

# create app
app = Flask(__name__, static_folder='static')
cors = flask_cors.CORS(app, resources={r"/api/*": {"origins": "*"}})

# routes
@app.route('/square/', methods=['POST', 'OPTIONS'])
@flask_cors.cross_origin()
def square():
    if request.method == "OPTIONS":  # CORS preflight
        return build_cors_prelight_response()

    # get data
    data = request.get_json()[0]
    num_list = data.values()

    response = {}
    response['results'] = []

    for n in num_list:
        square = n ** 2
        response['results'].append(square)

    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>My API Server</h1>"


def build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True)
