# from flask import Flask, request
# from log_writer import LogWriter

# app = Flask(__name__)
# log_writer = LogWriter()

# @app.route('/api/search', methods=['GET'])
# def search_api():
#     log_writer.write_log("info", "Inside the Search API", "log1.log")
#     return "Search API called"

# # Add more APIs as needed...

# if __name__ == '__main__':
#     app.run(port=5000)


from flask import Flask, request
from log_writer import LogWriter

app = Flask(__name__)
log_writer = LogWriter()

@app.route('/api/search', methods=['GET'])
def search_api():
    log_writer.write_log("info", "Inside the Search API", "log1.log")
    return "Search API called"

# Add more APIs as needed...

if __name__ == '__main__':
    app.run(port=5000)
