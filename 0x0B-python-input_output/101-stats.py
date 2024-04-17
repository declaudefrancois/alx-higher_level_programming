#!/usr/bin/python3
"""Reads stdin line by line and computes metrics.
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>.
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:

    Total file size: File size: <total size>
    where is the sum of all previous (see input format above)
    Number of lines by status code::
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear, don’t print anything for this
        status code format: <status code>: <number>
        status codes should be printed in ascending order
"""
import sys
import subprocess


def run():
    """Reads stdin line by line and computes metrics.
    """
    stats = {
        'size': 0,
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:
        i = 0
        for line in sys.stdin:
            status, size = line.strip('\n').split(' ')[-2:]
            stats['size'] += int(size)
            stats[status] += int(status)

            i += 1
            if i % 10 == 0:
                for key, value in stats.items():
                    if key == 'size':
                        print("File size: {}".format(stats.get('size')))
                    else:
                        print("{}: {}".format(key, value))
    except KeyboardInterrupt:
        for key, value in stats.items():
            if key == 'size':
                print("File size: {}".format(stats.get('size')))
            else:
                print("{}: {}".format(key, value))


if __name__ == "__main__":
    run()
