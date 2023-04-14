#!/usr/bin/python3
""" Define a script that reads stdin line by line and computes metrics"""


import sys
from collections import defaultdict


def compute_metrics():
    """
    Reads stdin line by line and computes metrics:
    - Total file size: File size: <total size>
    - Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code does not appear,
        do not print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
    """

    # Initialize variables to store metrics
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            # Parse input line
            ip, _, _, _, status, size = line.split()

            # Update metrics
            total_size += int(size)
            status_codes[status] += 1
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_codes.keys()):
                    print(f"{code}: {status_codes[code]}")

    except KeyboardInterrupt:
        # Print final metrics upon receiving a keyboard interruption
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")
