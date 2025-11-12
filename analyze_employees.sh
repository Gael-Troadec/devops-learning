#!/bin/bash

LOG_FILE="analyze_employees.log"

log_info() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') -INFO - $1" | tee -a "$LOG_FILE"
}

log_error() {
echo "$(date '+%Y-%m-%d %H:%M:%S') -ERROR - $1" | tee -a "$LOG_FILE"
}

log_info "Starting analyze_employees script"

CSV_FILE="${1:-employees.csv}"
MIN_SALARY="${2:-6000}"

if [ ! -f "$CSV_FILE" ]; then
    log_error "CSV file does not exist: $CSV_FILE"
    exit 1
fi

log_info "File found: $CSV_FILE, starting analysis"s

echo "=== EMPLOYEE DATA ANALYSIS ==="
echo ""

log_info "Counting total employees"
TOTAL_EMPLOYEES=$(wc -l < "$CSV_FILE")
echo "Total employees: $TOTAL_EMPLOYEES"

log_info "Counting admins"
ADMIN_COUNT=$(grep "admin" "$CSV_FILE" | wc -l)
echo "Admins: $ADMIN_COUNT"

log_info "Calculating average admin salary"
AVG_SALARY=$(awk -F, '/admin/ {sum+=$3; count++} END {if (count > 0) print sum/count; else print0}' "$CSV_FILE")
echo "Average admin salary: $AVG_SALARY"

log_info "Finding employees earning above $MIN_SALARY"
EMPLOYEES_ABOVE=$(awk -F, -v min=$MIN_SALARY '$3 > min {count++} END {print count}' "$CSV_FILE")
echo "Employees earning > $MIN_SALARY: $EMPLOYEES_ABOVE"

log_info "Analysis completed successfully"