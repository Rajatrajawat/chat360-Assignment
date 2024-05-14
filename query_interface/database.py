# import sqlite3

# def initialize_db():
#     conn = sqlite3.connect('logs.db')
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS logs (
#             level TEXT,
#             log_string TEXT,
#             timestamp TEXT,
#             source TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def insert_log(level, log_string, timestamp, source):
#     conn = sqlite3.connect('logs.db')
#     c = conn.cursor()
#     c.execute('INSERT INTO logs (level, log_string, timestamp, source) VALUES (?, ?, ?, ?)',
#               (level, log_string, timestamp, source))
#     conn.commit()
#     conn.close()






















import sqlite3

def initialize_db():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            level TEXT,
            log_string TEXT,
            timestamp TEXT,
            source TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_log(level, log_string, timestamp, source):
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('INSERT INTO logs (level, log_string, timestamp, source) VALUES (?, ?, ?, ?)',
              (level, log_string, timestamp, source))
    conn.commit()
    conn.close()
