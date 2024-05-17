#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Function to print statistics
def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

# Function to handle keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Bind the CTRL+C signal to the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Define a regex pattern for the expected log format
log_pattern = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
)

# Read from stdin line by line
try:
    for line_number, line in enumerate(sys.stdin, 1):
        match = log_pattern.match(line)
        if not match:
            continue

        ip, date, status, size = match.groups()
        status = int(status)
        size = int(size)

        # Update total file size and status code count
        total_size += size
        if status in status_codes:
            status_codes[status] += 1

        # Print statistics after every 10 lines
        if line_number % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle any additional keyboard interruptions
    print_stats()
    sys.exit(0)
