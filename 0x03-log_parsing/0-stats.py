#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_size = 0
status_codes = {}


# Define the signal handler for CTRL + C
def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)


# Define the function to print statistics
def print_stats():
    print("Total file size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


# Set the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read input from stdin line by line
for line_num, line in enumerate(sys.stdin, start=1):
    # Parse the input line
    try:
        ip, _, _, date, _, request, status_code, file_size, *_ = line.split()
        if request != "GET /projects/260 HTTP/1.1":
            continue
        file_size = int(file_size)
        status_code = int(status_code)
    except ValueError:
        continue

    # Update the total file size
    total_size += file_size

    # Update the status code count
    if status_code in status_codes:
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1

    # Print statistics every 10 lines
    if line_num % 10 == 0:
        print_stats()

# Print final statistics
print_stats()
