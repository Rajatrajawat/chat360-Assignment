# import subprocess

# # Start the log ingestor API
# subprocess.Popen(["python", "log_ingestor/api.py"])

# # Start the query interface
# subprocess.Popen(["python", "query_interface/web_ui.py"])











import subprocess

# Start the log ingestor API
subprocess.Popen(["python", "log_ingestor/api.py"])

# Start the query interface
subprocess.Popen(["python", "query_interface/web_ui.py"])






































# Find the process using port 5001:
# bash
# Copy code
# lsof -i :5001
# This will display the list of processes using that port. You can then kill the process by noting its PID and running:
# bash
# Copy code
# kill -9 <PID>
# Example:
# bash
# Copy code
# lsof -i :5001
# COMMAND   PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
# python3  12345 rajat   10u  IPv4 0x1c2ef45d6887340b      0t0  TCP *:commplex-link (LISTEN)
# To stop this process:
# bash
# Copy code
# kill -9 12345






# if __name__ == "__main__":
#     app.run(port=5002)
