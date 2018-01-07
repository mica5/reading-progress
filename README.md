# reading-progress
keep a timer that lets you know whether you're reading in time with the timer you set for yourself

requires the command-line `date` utility to work, so it should work in linux and mac out of the box, but I don't know if it can be made to work on windows.

For example:
$ python3 reading_progress.py '30minutes' 15 27

minutes per page: 2.31
pages per minute: 0.43
total pages: 13
start time: 2018-01-06 18:53:43.778496
finish time: 2018-01-06 19:23:43
current page | pages remaining | percentage complete | time remaining
        15.0 |            13.0 |                   0 | 0:29:54

In the output above, the last line keeps updating each second to show the new current page, pages remaining, percentage complete, and time remaining.
