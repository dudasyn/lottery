#!/usr/bin/env python
# Python 2/3 compatibility:
from __future__ import print_function, division
try:
    input = raw_input
except NameError:
    pass
from datetime import datetime

__doc__ = """\
Usage:   moonphase.py [year month day]
Using calculator from
http://gmmentalgym.blogspot.com/2013/01/moon-phase-for-any-date.html
which is based on Conway's moon phase algorithm from "Winning Ways for
your Mathematical Plays, Volume 2" (1980).
Estimate the age of the moon from 0 to 29 for a particular date
29,30=0,1 new moon
2-6 waxing crescent
7-8 first quarter
9-13 waxing gibbous
14-16 full
17-21 waning gibbous
22-23 last quarter
24-28 waning (de)crescent
If year, month and day are not provided, input is requested.
Handles years from 1700 to 3099.
"""
hmonths = {
    12: 'ADAR',
    5 : 'AV',
    6 : 'ELUL',
    8 : 'HESHVAN',
    2 : 'IYYAR',
    9 : 'KISLEV',
    1 : 'NISAN',
    11: 'SHEVAT',
    3 : 'SIVAN',
    4 : 'TAMMUZ',
    10: 'TEVETH',
    7 : 'TISHRI',
    13: 'VEADAR' }

def moonphase(year, month, day, do_print=False):
    h = year // 100             # integer division for the century
    yy = year % 100             # year within the century

    # The "golden number" for this year is the year modulo 19, but
    # adjusted to be centered around 0 -- i.e., -9 to 9 instead
    # of 0 to 19.  This improves the accuracy of the approximation
    # to within +/- 1 day.
    g = (yy + 9) % 19 - 9

    # There is an interesting 6 century near-repetition in the
    # century correction.  It would be interesting to find a
    # algorithm that handles the different corrections between
    # centuries 17|23|29, 20|26, 21|27, and 24|30.

    try:
        c = {17:7,
             18:1, 19:-4, 20:-8, 21:16, 22:11, 23:6,
             24:1, 25:-4, 26:-9, 27:15, 28:11, 29:6,
             30:0}[h]
    except KeyError:
        print("No century correction available for {}00-{}99".format(h,h))
        return

    # Golden number correction:  modulo 30, from -29 to 29.
    gc = g * 11
    #old while ( gc < -29 ): gc += 30;
    #old if (gc > 0): gc %= 30;
    while ( gc < -29 ): gc += 30
    if (gc > 0): gc %= 30

    # January/February correction:
    if month < 3:
       mc = 2
    else:
       mc = 0

    phase = (month + mc + day + gc + c + 30 ) % 30

    return phase

def get_name_of_moon(phase):
        if phase < 2:
            return("New moon [or slightly after]")
        elif phase < 7:
            return("Waxing crescent")
        elif phase < 9:
            return("First quarter")
        elif phase < 14:
            return("Waxing gibbous")
        elif phase < 16:
            return("Full moon")
        elif phase < 22:
            return("Waning gibbous")
        elif phase < 24:
            return("Last quarter")
        elif phase < 29:
            return("Waning (de)crescent")
        elif phase < 31:
            return("New moon [or slightly before]")