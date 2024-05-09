#!/usr/bin/python3
"""script that reads `stdin` line by line and computes metrics"""

import sys


def print_statistics(total_file_size, status_code_count):
    """
    Print statistics including total file size and number of
    lines by status code.
    Args:
        total_file_size (int): The total file size.
        status_code_count (dict): A dictionary containing the
        count of each status code.
    Returns:
        None
    """
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_count):
        print("{}: {}".format(status_code, status_code_count[status_code]))


def parse_line(line, total_file_size, status_code_count):
    """
    Parse a line from stdin and update total file size and
    status code count accordingly.
    Args:
        line (str): The line read from stdin.
        total_file_size (int): The current total file size.
        status_code_count (dict): A dictionary containing the
        count of each status code.
    Returns:
        int: The updated total file size.
        dict: The updated status code count.
    """
    split_line = line.split()
    if len(split_line) != 10:
        return total_file_size, status_code_count

    try:
        status_code = int(split_line[8])
        file_size = int(split_line[9])
    except ValueError:
        return total_file_size, status_code_count

    total_file_size += file_size
    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
        status_code_count[status_code] = status_code_count.get(status_code,
                                                               0) + 1

    return total_file_size, status_code_count


def main():
    """
    Main function to read stdin, parse each line, and print statistics.
    """
    total_file_size = 0
    status_code_count = {}
    line_count = 0

    try:
        for line in sys.stdin:
            total_file_size, status_code_count = parse_line(line.strip(),
                                                            total_file_size,
                                                            status_code_count)
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_count)
                print()

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_count)


if __name__ == "__main__":
    main()
