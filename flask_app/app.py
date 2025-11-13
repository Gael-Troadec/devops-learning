#!usr/bin/env python3

import psutil
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
    
@app.route('/health')
def health():
    try:
        logger.info("User requested /health endpoint")

        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        health_data = {
            "status": "OK",
            "timestamp": datetime.now().isoformat(),
            "cpu_usage_percent": cpu_percent,
            "memory_used_gb": round(memory.used / (1024 ** 3), 2),
            "memory_total_gb": round(memory.total / (1024 ** 3), 2),
            "memory_percent": memory.percent,
            "disk_used_gb": round(disk.used / (1024 ** 3), 2),
            "disk_total_gb": round(disk.total / (1024 ** 3), 2),
            "disk_percent": disk.percent
        }

        logger.info("Health check completed successfully")
        return health_data
    
    except Exception as e:
        logger.error(f"Error in health check: {e}")
        return {"status": "ERROR", "message": str(e)}, 500

@app.route('/health/dashboard')
def health_dashboard():
    try:
        logger.info("User requested /health/dashboard endpoint")

        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>System Health Dashboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .metric {{ margin: 20px 0; padding: 10px; background: #f0f0f0; border-radius: 5px; }}
                .ok {{ color: green; }}
                .warning {{ color: orange; }}
                .critical {{ color: red; }}
            </style>
        </head>
        <body>
            <h1>System Health Dashboard</h1>
            <p>Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

            <div class="metric">
                <h2>CPU Usage</h2>
                <p class="{'critical' if cpu_percent > 80 else 'warning' if cpu_percent > 50 else 'ok'}">{cpu_percent}%</p>
            </div>

            <div class="metric">
                <h2>Memory Usage</h2>
                <p>{memory.used / (1024 ** 3):.2f} GB / {memory.total / (1024 ** 3):.2f} GB / ({memory.percent}%)</p>
                <p class="{'critical' if memory.percent > 80 else 'warning' if memory.percent > 50 else 'ok'}">Status: {'CRITICAL' if memory.percent > 80 else 'WARNING' if memory.percent > 50 else 'ok'}</p>
            </div>

            <div class="metric">
                <h2>Disk Usage</h2>
                <p>{disk.used / (1024 ** 3):.2f} GB / {disk.total / (1024 ** 3):.2f} GB ({disk.percent}%)</p>
                <p class="{'critical' if disk.percent > 80 else 'warning' if disk.percent > 50 else 'ok'}">Status: {'CRITICAL' if disk.percent > 80 else 'WARNING' if disk.percent > 50 else 'OK'}</p>
            </div>
        </body>
        </html>
        """

        logger.info("DASHBOARD generated successfully")
        return html
    
    except Exception as e:
        logger.error(f"Error generating dashboard: {e}")
        return f"<h1>Error</h1><p>{str(e)}</p>", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)