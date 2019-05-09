'''
Created on Sep 4, 2018

This is a program for determining the pricing and the arrival and departure time of the school bus to a specified location. 
The rules of the bus operation and the requirements on the program are described below. 

The bus arrives at the first stop exactly 45 minutes prior to the time when the school starts. 
The bus spends 2 minutes at each stop waiting for the students to get on 
and 3 minutes traveling between any two consecutive stops. 
All school bus stops are numbered and each customer knows their stop number.
The cost of the school bus ticket equals $1 plus 15 cents for each full 4 minute interval spent traveling from the stop to the school. 
Note that the waiting time at the stop where the student gets in, is not charged.

@author: lufei (Luna) Guan
'''
# inputs
HourStarts = eval(input('Please enter the hour when school starts:'))
MinuteStarts = eval(input('Please enter the minute when school starts:'))
StopNumber = eval(input('Please enter your stop number:'))

# constants
TotalTime = 45 # in minute
TravelTime = 3 # in minute
WaitingTime = 2 # in minute
BaseCost = 1 # in dollar
TimeIncrement = 4 # in minute
CostIncrement = 0.15 # in dollar

StartTime = HourStarts * 60 + MinuteStarts # in minute

ArrivalTime = StartTime - TotalTime + (StopNumber - 1) * (TravelTime + WaitingTime) # in minute
ArrivalHour = ArrivalTime // 60
ArrivalMinute = ArrivalTime % 60

DepartureTime = ArrivalTime + WaitingTime # in minute
DepartureHour = DepartureTime // 60
DepartureMinute = DepartureTime % 60

TripLength = StartTime - DepartureTime

TotalCost = (TripLength // TimeIncrement * CostIncrement) + BaseCost # in dollar

print('The bus will be at stop number', StopNumber, 'between', end = ' ')
print(ArrivalHour, ':', str(ArrivalMinute).zfill(2), sep = '', end = ' ')
print('and', end = ' ')
print(DepartureHour, ':', str(DepartureMinute).zfill(2), sep = '')

print('The length of the trip from stop number', StopNumber, 'is', TripLength, 'minutes')

print('The cost of the ticket from stop number', StopNumber, 'is', end = ' ')
print('$', TotalCost, sep = '')
