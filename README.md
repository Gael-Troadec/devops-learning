# Rover-Failsafe (Learning Project)

**Status:** Educational / Experimental  
**Purpose:** Learning Bash scripting, system design, failsafe mechanisms  
**Date:** November 2025  

## Overview
A conceptual failsafe system for an autonomous rover with health monitoring and graceful degradation.

**Note:** This is a learning project created while transitioning to DevOps. 
The architecture and concepts are valid, but this is not production-ready code.

## What I learned
- Bash scripting (process management, signal handling)
- JSON logging for system events
- Health check patterns
- Graceful shutdown and recovery

## Architecture
- `earth_server.sh` - Main server with failsafe logic
- Health monitoring every 30 seconds
- Graceful shutdown after 3 consecutive failures
- JSON structured logging

## How to run
```bash
bash earth_server.sh
```

## Next Steps
- Add proper error handling
- Implement Docker containerization
- Add comprehensive testing
- Create monitoring dashboard
