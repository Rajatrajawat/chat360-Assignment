# from flask import Flask, request, jsonify
# from query_service import search_logs

# app = Flask(__name__)

# @app.route('/search', methods=['GET'])
# def search():
#     level = request.args.get('level')
#     log_string = request.args.get('log_string')
#     start_timestamp = request.args.get('start_timestamp')
#     end_timestamp = request.args.get('end_timestamp')
#     source = request.args.get('source')
#     results = search_logs(level, log_string, start_timestamp, end_timestamp, source)
#     return jsonify(results)

# if __name__ == '__main__':
#     app.run(port=5001)

































from flask import Flask, request, jsonify
from query_service import search_logs

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    level = request.args.get('level')
    log_string = request.args.get('log_string')
    start_timestamp = request.args.get('start_timestamp')
    end_timestamp = request.args.get('end_timestamp')
    source = request.args.get('source')
    results = search_logs(level, log_string, start_timestamp, end_timestamp, source)
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5001)
