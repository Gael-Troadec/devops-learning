#!usr/bin/env python3

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('flask_app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps!"

@app.route('/about')
def about():
    logger.info("User visited about page")
    return "This is the about page"

@app.route('/status')
def status():
    logger.info("User requested status")
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Server is running at {current_time}"

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    try:
        logger.info(f"User requested division: {a}/{b}")
        result = a / b
        logger.info(f"Division successful: {a}/{b} = {result}")
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        logger.error(f"Division by zero attempted: {a}/{b}")
        return "Error: Division by zero", 400
    except Exception as e:
        logger.error(f"Unexpected error in division: {e}")
        return "Error: Something went wrong", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)