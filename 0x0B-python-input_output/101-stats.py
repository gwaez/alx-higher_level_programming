#!/usr/bin/python3
# 101-stats.py
# Ahmed Mahmoud - Gwaez
import sys

def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            data = line.split()
            if len(data) >= 8:
                status_code = data[-2]
                file_size = int(data[-1])

                total_size += file_size
                status_counts[status_code] += 1

            if i % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
