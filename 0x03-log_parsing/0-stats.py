#!/usr/bin/python3
"""
log parsing
"""

import sys


if __name__ == '__main__':

    total_size, lines_processed = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {i: 0 for i in codes}

    def print_statistics(stats: dict, total_size: int) -> None:
        """
		function to display stats
        """
        print(f'File size: {total_size}')
        for i, j in sorted(stats.items()):
            if j:
                print(f'{i}: {j}')

    try:
        for line in sys.stdin:
            lines_processed += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                total_size += int(data[-1])
            except BaseException:
                pass
            if lines_processed % 10 == 0:
                print_statistics(stats, total_size)
        print_statistics(stats, total_size)
    except KeyboardInterrupt:
        print_statistics(stats, total_size)
        raise
