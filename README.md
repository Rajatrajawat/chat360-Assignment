# Log Control System

## Overview
This project implements a logging system with multiple APIs and a query interface for searching logs.

## Project Structure
- `log_ingestor/`: Contains the log ingestor API and related files.
- `query_interface/`: Contains the query interface and database-related files.
- `logs/`: Directory to store log files.
- `main.py`: Script to run both services.
- `README.md`: This file.

## Setup and Running the Project

### Prerequisites
- Python 3.7+
- Flask

### Setup
1. Create a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
