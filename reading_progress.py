#!/usr/bin/env python3
"""calculate the page that reader should currently be on

input - time remaining, current page, final page
output - always display page that should be currently displayed, rounded to one decimal point

Version 0.1
2018-01-06
"""
import argparse
import datetime
from dateutil.parser import parse
from time import sleep
import subprocess

one_minute = datetime.timedelta(minutes=1)

def convert_reltime_to_abstime(string):
    """
    example use cases:
        in reminders command
        in events command
    """
    return subprocess.check_output([
        'date', '-d{}'.format(string)
    ]).decode().strip()

def run_main():
    args = parse_cl_args()

    finish_time = parse(convert_reltime_to_abstime(args.time_remaining), ignoretz=True)
    time_remaining = finish_time - datetime.datetime.now()
    start_page = args.current_page
    final_page = args.final_page + 1

    start_time = datetime.datetime.now()

    num_pages = final_page - start_page
    time_per_page = time_remaining / num_pages
    now = datetime.datetime.now()

    minutes = time_remaining / one_minute
    minutes_per_page = minutes / num_pages
    print('minutes per page: {:.2f}'.format(minutes_per_page))
    pages_per_minute = num_pages / minutes
    print('pages per minute: {:.2f}'.format(pages_per_minute))
    print('total pages:', num_pages)
    print('start time: {}'.format(start_time.replace(microsecond=0)))
    print('finish time: {}'.format(finish_time))

    seconds_between_prints = args.seconds_between_prints
    print(' | '.join([
        'current page',
        'pages remaining',
        'percentage complete',
        'time remaining',
    ]))
    while now < finish_time:
        time_remaining = finish_time - now
        current_page = final_page - (time_remaining / time_per_page)
        pages_remaining = final_page - current_page
        percentage_complete = (current_page - start_page) / (final_page - start_page) * 100
        print('\r' + ' | '.join([
            '{current_page:12.1f}',
            '{pages_remaining:15.1f}',
            '{percentage_complete:19.0f}',
            '{time_remaining}',
        ]).format(
            current_page=current_page,
            pages_remaining=pages_remaining,
            percentage_complete=percentage_complete,
            # chop off the seconds decimal
            time_remaining=datetime.timedelta(seconds=time_remaining.seconds),
        ), end='')

        sleep(seconds_between_prints)
        now = datetime.datetime.now()

    print('finished at {}'.format(now))

    success = True
    return success

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    argParser.add_argument('time_remaining')
    argParser.add_argument('current_page', type=int)
    argParser.add_argument('final_page', type=int)
    argParser.add_argument('-s', '--seconds-between-prints', type=float, default=1)

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)

