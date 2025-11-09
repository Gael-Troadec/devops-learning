import json
import subprocess
from datetime import datetime

def check_server_health(logfile):
    """Analyze server logs for health issues"""

    print("=== SERVER HEALTH MONITOR ===\n")

    # Count errors by type
    result = subprocess.run(['grep', 'ERROR', logfile], capture_output=True, text=True)
    errors = {}
    for line in result.stdout.strip().split('\n'):
        if line:
            error_type = line.split('[')[1].split(']')[0]
            errors[error_type] = errors.get(error_type, 0) + 1

    # Alert if critical
    alert_level = "OK"
    if sum(errors.values()) > 5:
        alert_level = "WARNING"
    if sum(errors.values()) > 10:
        alert_level = "CRITICAL"

    # Generate report
    report = {
        "timestamp": datetime.now().isoformat(),
        "alert_level": alert_level,
        "totale_errors": sum(errors.values()),
        "error_breakdown": errors
    }

    return report

if __name__ == "__main__":
    report = check_server_health("server_logs.txt")
    print(f"Alert level: {report['alert_level']}")
    print(f"Total Errors: {report['totale_errors']}")
    print(f"Errors: {report['error_breakdown']}\n")

    # Save report as JSON
    with open("health_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Report saved to health_report.json")    

