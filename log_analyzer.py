import subprocess
import sys 

def analyze_logs(logfile):
    print(f"=== LOG ANALYSIS: {logfile} ===\n")

    # Compte les erreurs
    result = subprocess.run(['grep', 'ERROR', logfile], capture_output=True, text=True)
    errors = result.stdout.strip().split('\n') if result.stdout else []
    error_count = len([e for e in errors if e])
    print(f"Total ERRORs: {error_count}")

    # Compte les warnings
    result = subprocess.run(['grep', 'WARNING', logfile], capture_output=True, text=True)
    warnings = result.stdout.strip().split('\n') if result.stdout else []
    warning_count = len([w for w in warnings if w])
    print(f"Total WARNINGs: {warning_count}\n")

    # Liste les IPs qui ont echoue
    print("Failed login IPs:")
    result = subprocess.run(['grep', 'Failed login', logfile], capture_output=True, text=True)
    for line in result.stdout.strip().split('\n'):
        if line :
            ip = line.split()[-1]
            print(f" - {ip}")

    print("\nError types:")
    result = subprocess.run(['grep', 'ERROR', logfile], capture_output=True, text=True)
    for line in result.stdout.strip().split('\n'):
        if line:
            error_type = line.split('[')[1].split(']')[0]
            print(f" - {error_type}")

    error_breakdown = count_errors_by_type(logfile)
    print("\nError breakdown:")
    for error_type, count in error_breakdown.items():
        print(f"  - {error_type}: {count}")

def count_errors_by_type(logfile):
    result = subprocess.run(['grep', 'ERROR', logfile], capture_output=True, text=True)
    error_types = {}
    for line in result.stdout.strip().split('\n'):
        if line:
            error_type = line.split('[')[1].split(']')[0]
            error_types[error_type] = error_types.get(error_type, 0) + 1
    return error_types

if __name__ == "__main__":
    logfile = sys.argv[1] if len(sys.argv) > 1 else "server_logs.txt"
    analyze_logs(logfile)
