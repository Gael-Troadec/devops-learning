#!/bin/bash

echo "=== SYSTEM INFO ==="
echo "Hostname: $(hostname)"
echo "OS: $(uname -s)"
echo "Kernel: $(uname -r)"
echo "CPU cores: $(nproc)"
echo "Uptime: $(uptime)"
echo "Free memory: $(free -h | grep Mem | awk '{print $7}')"
echo "Disk usage: $(df -h / | tail -1 | awk '{print $5}')"
