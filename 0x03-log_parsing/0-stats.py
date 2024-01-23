#!/usr/bin/python3
import sys


def print_stats(total_size, status_code_counts):
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))


def parse_line(line, total_size, status_code_counts):
    try:
        parts = line.split()
        if len(parts) != 9 or parts[2] != "GET" or parts[3] \
                != "/projects/260" or parts[5] != "HTTP/1.1":
            return total_size, status_code_counts  # Skip invalid lines

        status_code = int(parts[7])
        file_size = int(parts[8])

        total_size += file_size

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_code_counts[status_code] = \
                status_code_counts.get(status_code, 0) + 1

    except ValueError:
        pass  # Ignore lines with invalid integer values

    return total_size, status_code_counts


def main():
    total_size = 0
    status_code_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_code_counts = parse_line(line.strip(),
                                                total_size, status_code_counts)
            if i % 10 == 0:
                print_stats(total_size, status_code_counts)

    except KeyboardInterrupt:
        pass  # Handle CTRL + C

    finally:
        print_stats(total_size, status_code_counts)


if __name__ == "__main__":
    main()
