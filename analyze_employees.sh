#!/bin/bash

FILE="${1:-employees.csv}"
MIN_SALARY="${2:-6000}"

echo "=== EMPLOYEE DATA ANALYSIS ==="
echo ""

echo "Total employees:"
wc -l < $FILE

echo ""
echo "Admins:"
grep "admin" $FILE | wc -l

echo ""
echo "Average admin salary:"
awk -F: '/admin/ {sum+=$3; count++} END {print sum/count}' $FILE

echo ""
echo "Employees earning > $MIN_SALARY:"
awk -F: -v min=$MIN_SALARY '$3 > min {print $1, $3}' $FILE
