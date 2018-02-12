# Python Savings
A simple python script to help with saving money through the year

## How it works
This is a basic command line script I came up with to help me when I was struggling with a new method for saving money through the year.

The basic idea is to save 1p on Jan 1st, 2p on Jan 2nd and so on until you save £3.64 on December 31st (by which time you should have saved £667.95). When I began I was doing it mentally and struggling to remember if I had done it the day before so was having to add all the previous days and check against the total I had already.

This wasn't a long term solution so I decided to create a simple python script that would tell me three things: how much the total should be, how much should be saved on that day, and the simplest way to make in the smallest number of coins.

An example of the output would be:

'''
Today's date is Feb 12 2018 which means it is day 43 of this year
You should add £0.43 to your savings today, meaning your total should be £9.46

The easiest way to make this is to use the following coins:
£2 x4
£1 x1
20p x2
5p x1
1p x1
'''
