#!/usr/bin/env python

# File:         chap08pp1.py
# Author:       Prof. M. Darden
# Date:         2013-09-30
# Description:  Solution to Programming Project #1, from Chapter 8 of the text


def get_data_list(file_name):
    # A different take on function provided in the book
    with open(file_name) as data_file:
        data_list = [line.strip().split(',') for line in data_file]
    return data_list


def get_monthly_averages(data_list):
    # Define and initialize some working variables
    monthly_averages_list = []
    month = None
    year = None
    num = 0
    den = 0

    # Loop through each date in file and calculate monthly average price
    for datum in data_list[1:]:
        y, m, d = datum[0].split('-')

        # When month changes, record previously gathered information
        if m != month:
            if month is not None:
                avg = num / den
                monthly_averages_list.append((avg, '{}-{}'.format(year, month)))
                num = 0
                den = 0
            year = y
            month = m

        # Update monthly average price with a single day's info
        volume = int(datum[5])
        adjusted_close = float(datum[6])
        num += volume * adjusted_close
        den += volume

    return monthly_averages_list


def print_info(monthly_averages_list):
    monthly_averages_list.sort(reverse=True)

    print('\nBest 6 Months:')
    for i in range(6):
        print('{1}\t${0:.2f}'.format(*monthly_averages_list[i]))

    print('\nWorst 6 Months:')
    for i in range(-7, -1):
        print('{1}\t${0:.2f}'.format(*monthly_averages_list[i]))


def main():
    data_list = get_data_list('table.csv')
    # print(data_list)
    mal = get_monthly_averages(data_list)
    # print(mal)
    print('Google Stock Price Averages')
    print('===========================')
    print_info(mal)

if __name__ == '__main__':
    main()
