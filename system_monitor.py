#!/usr/bin/env python3

import psutil
import json
import sys
from datetime import datetime
import logging

# Configure logging to weite to both file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('system_monitor.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def get_system_info():
    try:
        logger.info("Starting system monitoring")
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()

        memory = psutil.virtual_memory()
        memory_used_gb = memory.used / (1024 ** 3)
        memory_total_gb = memory.total / (1024 ** 3)
        memory_percent = memory.percent

        disk = psutil.disk_usage('/')
        disk_used_gb = disk.used / (1024 ** 3)
        disk_total_gb = disk.total / (1024 ** 3)
        disk_percent = disk.percent

        hostname = psutil.os.uname().nodename

        try:
            battery = psutil.sensors_battery()
            if battery:
                battery_info = {"percent": battery.percent, "status": "charging" if battery.power_plugged else "discharging"}
            else:
                battery_info = {"percent": None, "status": "N/A"}
        except:
            battery_info = {"percent": None, "status": "N/A"}

        logger.info("System monitoring completed successfully")

        return {
        "timestamp": datetime.now().isoformat(),
        "cpu": {"usage": cpu_percent, "cores": cpu_count},
        "memory": {"used_gb": round(memory_used_gb, 2), "total_gb": round(memory_total_gb, 2), "percent": memory_percent},
        "disk": {"used_gb": round(disk_used_gb, 2), "total_gb": round(disk_total_gb, 2), "percent": disk_percent},
        "system": {"hostname": hostname},
        "battery": battery_info, 
    }
    except Exception as e:
        logger.error(f"Error during system monitoring: {e}")
        sys.exit(1)

def get_alert_level(data):
    cpu = data["cpu"]["usage"]
    memory_percent = data["memory"]["percent"]
    disk_percent = data["disk"]["percent"]

    max_usage = max(cpu, memory_percent, disk_percent)

    if max_usage >= 95:
        return 2, "CRITICAL"
    elif max_usage >= 80:
        return 1, "WARNING"
    else:
        return 0, "OK"
    
def main():
    data = get_system_info()
    exit_code, alert_statuts = get_alert_level(data)

    data["alert"] = alert_statuts

    print(json.dumps(data, indent=2))
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

