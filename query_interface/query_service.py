# import sqlite3

# def search_logs(level=None, log_string=None, start_timestamp=None, end_timestamp=None, source=None):
#     query = "SELECT * FROM logs WHERE 1=1"
#     params = []
#     if level:
#         query += " AND level=?"
#         params.append(level)
#     if log_string:
#         query += " AND log_string LIKE ?"
#         params.append(f"%{log_string}%")
#     if start_timestamp and end_timestamp:
#         query += " AND timestamp BETWEEN ? AND ?"
#         params.append(start_timestamp)
#         params.append(end_timestamp)
#     if source:
#         query += " AND source=?"
#         params.append(source)
#     conn = sqlite3.connect('logs.db')
#     c = conn.cursor()
#     c.execute(query, params)
#     results = c.fetchall()
#     conn.close()
#     return results






























import sqlite3

def search_logs(level=None, log_string=None, start_timestamp=None, end_timestamp=None, source=None):
    query = "SELECT * FROM logs WHERE 1=1"
    params = []
    if level:
        query += " AND level=?"
        params.append(level)
    if log_string:
        query += " AND log_string LIKE ?"
        params.append(f"%{log_string}%")
    if start_timestamp and end_timestamp:
        query += " AND timestamp BETWEEN ? AND ?"
        params.append(start_timestamp)
        params.append(end_timestamp)
    if source:
        query += " AND source=?"
        params.append(source)
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute(query, params)
    results = c.fetchall()
    conn.close()
    return results
