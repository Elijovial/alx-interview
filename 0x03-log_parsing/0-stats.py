#!/usr/bin/python3
import sys
import signal

# Initialize a dictionary to store file size and status code counts
stats = {"file_size": 0, "status_codes": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}}

# Function to print the statistics
def print_stats():
    print("File size: {}".format(stats["file_size"]))
    for code in sorted(stats["status_codes"].keys()):
        if stats["status_codes"][code] > 0:
            print("{}: {}".format(code, stats["status_codes"][code]))

# Function to handle CTRL+C interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Bind the CTRL+C signal to the signal_handler function
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
line_count = 0
try:
    for line in sys.stdin:
        try:
            parts = line.split()
            ip, date, method, status, size = parts[0], parts[1], parts[3], parts[5], parts[6]
            if method == '"GET' and "/projects/260" in line:
                stats["file_size"] += int(size)
                if status in stats["status_codes"]:
                    stats["status_codes"][status] += 1
        except (IndexError, ValueError):
            continue
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
