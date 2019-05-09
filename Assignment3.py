'''
Created on Sep 30, 2018

Assignment 3

Processing order data from a fictional coffee shop.
Optimize the business operations.

The program will work as follows:
1. Ask the user how many days of data to summarize.
2.Create and display the order summary matrix, summarizing how many orders were placed during each one-hour
interval starting from 6am and ending at midnight, for each day starting from the first of the month until
the day number, provided by the user in step 1. Recall, that each row in the ORDERS list presents one order.
3.Ask the user to specify the data, for which a histogram will be displayed. The histogram displays each 
order as one * symbol. Repeat step 3, until -1 is entered.

@author: lufei Guan
'''

import orderlog
ORDERS = orderlog.orderlst
timeOpen = 6*60 # open time in minutes
timeClose = 24*60   # close time in minutes
lenOfTimeInterval = 60  # length of time interval in minutes

### compose order summary matrix--------------------------------------------------
def composeOrderMatrix(numOfDays = 31): # default value is 31
    numOfTimeInterval = int((timeClose - timeOpen)/lenOfTimeInterval)
    
    # time transform to mins
    ORDERS.remove(ORDERS[0])
     
    tmatrix = []    # create an empty matrix for time
    for jr in range(len(ORDERS)):
        tmatrix.append([])
        for jc in range(2):
            value = 0
            tmatrix[jr].append(value)
            
    for i in range(len(ORDERS)):
        order1 = ORDERS[i][0].split(' ')  # only date and time, split already
        tmatrix[i][0] = order1
        hour = int(order1[1][0:2])
        minute = int(order1[1][3:5])
        hrToMinute = hour*60 + minute
        tmatrix[i][1] = hrToMinute
     
    # # count orders
    matrix = [[0 for col in range (numOfDays)] for row in range (numOfTimeInterval)]
     
    for i in range(len(ORDERS)):
        day = int(tmatrix[i][0][0][8:])
        time = tmatrix[i][1]
        row = int((time//lenOfTimeInterval)-(timeOpen/lenOfTimeInterval)+1)
        if day <= numOfDays:
            matrix[row-1][day-1] += 1

    return (matrix)


### print order summary matrix-----------------------------------------------------------
def printOrderSummaryMatrix(matrix):

    length = len(matrix[0]) + 1

    print('\n','ORDER SUMMARY'.center(12+length*3),'\n') 
      
    print('TIME \\ DAY'.center(15), '|'+ ''.join('%3s'%str(d) for d in range(1, length)))
    print('------------------'+''.join('---' for d in range(1, length)))
    
    
    for r in range(len(matrix)):
        h1 = str((timeOpen+lenOfTimeInterval*r)//60)
        m1 = str((timeOpen+lenOfTimeInterval*r)%60)
        h2 = str((timeOpen+(r+1)*lenOfTimeInterval-1)//60)
        m2 = str((timeOpen+(r+1)*lenOfTimeInterval-1)%60)
        print((h1+':'+m1.zfill(2)+' - '+h2+':'+m2.zfill(2)).rjust(15),
              '|'+ ''.join('%3s'%matrix[r][i] for i in range(0, length-1)))


### print histogram----------------------------------------------------------------------------
def printHistogram(matrix, day = 0):

    print('\n',('NUMBER OF ORDERS PER '+ str(lenOfTimeInterval)+ ' min FOR DAY '+ str(day)).center(60),'\n')
     
    for r in range(len(matrix)):
            h1 = str((timeOpen+lenOfTimeInterval*r)//60)
            m1 = str((timeOpen+lenOfTimeInterval*r)%60)
            h2 = str((timeOpen+(r+1)*lenOfTimeInterval-1)//60)
            m2 = str((timeOpen+(r+1)*lenOfTimeInterval-1)%60)
            print((h1+':'+m1.zfill(2)+' - '+h2+':'+m2.zfill(2)).rjust(15),
                  '|',''.join('*' for x in range(matrix[r][day-1])))
            

### main flow--------------------------------------------------------------------------------------
def Main():
    
    howManyDays = eval(input('How many days would you like to include?'))
    
    while howManyDays > 31:
        howManyDays = eval(input('How many days would you like to include?'))
    else:
        orderMatrix = composeOrderMatrix(howManyDays)
        printOrderSummaryMatrix(orderMatrix)
    
    enterDayNumber = eval(input('\nEnter day number from 1 to '+ str(howManyDays) +' to see a histogram, or -1 to exit:'))
    
    
    while enterDayNumber != -1:
        if enterDayNumber > howManyDays:
            enterDayNumber = eval(input('Enter day number from 1 to '+ str(howManyDays) +' to see a histogram, or -1 to exit:'))
    
        elif enterDayNumber <= howManyDays:
            printHistogram(orderMatrix, enterDayNumber)
            enterDayNumber = eval(input('\nEnter day number from 1 to '+ str(howManyDays) +' to see a histogram, or -1 to exit:'))
    else:
        print('Bye!')      
### end---------------------------------------------------------------------------------------------

Main()