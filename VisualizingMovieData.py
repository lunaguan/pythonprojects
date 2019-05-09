'''
Created on Dec 5, 2018

Create plots visualizing movie data

@author: lufei Guan
'''

TITLE = 'Title'

def pickMovieWithKeyword (folderName):
    import pandas as pd
    import os
    os.chdir(os.getcwd()+'\\'+folderName)
    movieInfo = pd.read_csv('IMDB.csv')
    
    print('\nPlot1: ratings by age group')
    totalNumOfMovies = len(movieInfo)
    selectNumOfMovies = eval (input ('How many of the '+ str( totalNumOfMovies) + ' movies would you like to consider?'))
    print('Select', selectNumOfMovies, 'movies')
    movieDFForPlot1 = pd.DataFrame()
    
    for i in range(selectNumOfMovies):  # select each movie with keywords one by one
        keyword = input ('\nEnter movie keyword:')
        selectMovieDF = movieInfo[movieInfo[TITLE].str.contains(keyword, case = False)] # search for keywords in the movie title
        
        while  len(selectMovieDF) == 0: # to make sure the keyword exists, if not, ask user to input another keyword.
            keyword = input ('\nEnter movie keyword:')
            selectMovieDF = movieInfo[movieInfo[TITLE].str.contains(keyword, case = False)]
        
        print('Which of the following movies would you like to pick (enter number)')
        
        selectMovieListDF = pd.DataFrame()
         
        for j in range(len(selectMovieDF)): # print each record of the selected movies with keyword
            numAndTitle = str(j+1).rjust(9)+' '+ selectMovieDF[TITLE].iloc[j]
            print(numAndTitle) 
            selectMovieListDF = selectMovieListDF.append(selectMovieDF.iloc[j,:])

        movieNum = eval(input('Enter a number:'))
        
        movieDFForPlot1 = movieDFForPlot1.append(selectMovieListDF.iloc[movieNum-1,:]) # store the movie info for later use
        movieTitle = selectMovieListDF[TITLE].iloc[movieNum-1]
        print('Movie #'+ str(i+1) +':  \''+movieTitle+'\'')
        
    return movieDFForPlot1



def plot1(movieDFForPlot1):
    import matplotlib.pyplot as plt
    x = ['<18', '18-29', '30-44', '>44']
    for i in range(len(movieDFForPlot1)): # find record for each selected movie
        y = movieDFForPlot1[['VotesU18', 'Votes1829', 'Votes3044', 'Votes45A']].iloc[i, :]
        plt.plot(x, y)
        plt.scatter(x, y, marker = 'o')
        mark = movieDFForPlot1[TITLE].iloc[i] + '('+movieDFForPlot1['Genre1'].iloc[i]+')'
        plt.annotate(mark, (x[0], y[0]))
        
    plt.xlabel('Age range')
    plt.ylabel('Rating')
    plt.title('Ratings by age group')
    plt.grid(color = 'lightgray', linestyle = '--', linewidth = .5)
    plt.savefig('plot1.jpg')
    
    return

# plot1(movieDFForPlot1)

def plot2():
    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    
    movieInfo = pd.read_csv('IMDB.csv')
    
    print('Plot2: Percentage of raters within gender-age. Select a movie:')
    
          
    keyword = input('\nEnter movie keyword: ')
    movieRecord = movieInfo[movieInfo[TITLE].str.contains(keyword, case = False)] # search for keyword in movie titles, and get movie record if keyword is included
    movieDFForPlot2 = pd.DataFrame()
    
    while  len(movieRecord) == 0: # make sure keyword exists in the file, if not, keep asking for another keyword
        keyword = input ('\nEnter movie keyword:')
        movieRecord = movieInfo[movieInfo[TITLE].str.contains(keyword, case = False)]
    
    if len(movieRecord) > 1: # if more than 1 movie, ask user to select which one to use. 
        print('Which of the following movies would you like to pick (enter number)')    
        selectMovieListDF = pd.DataFrame()
         
        for j in range(len(movieRecord)):
            numAndTitle = str(j+1).rjust(9)+' '+ movieRecord[TITLE].iloc[j]
            print(numAndTitle) 
            selectMovieListDF = selectMovieListDF.append(movieRecord.iloc[j,:])

        movieNum = eval(input('Enter a number:'))
        
        movieDFForPlot2 = movieDFForPlot2.append(selectMovieListDF.iloc[movieNum-1,:])
        movieTitle = selectMovieListDF[TITLE].iloc[movieNum-1]
        print('Movie #1: \''+movieTitle+'\'')
        
    else:    # if only 1 movie returned, print movie title and get plot directly.
        movieTitle = movieRecord[TITLE].iloc[0]
        print('Movie #1: \''+movieTitle+'\'')
    
    xf = ['<18f', '18-29f', '30-44f', '>44f']
    xm = ['<18m', '18-29m', '30-44m', '>44m']
    f1 = movieRecord['CVotesU18F'].iloc[0]  # get values required from the file.
    f2 = movieRecord['CVotes1829F'].iloc[0]
    f3 = movieRecord['CVotes3044F'].iloc[0]
    f4 = movieRecord['CVotes45AF'].iloc[0]
    m1 = movieRecord['CVotesU18M'].iloc[0]
    m2 = movieRecord['CVotes1829M'].iloc[0]
    m3 = movieRecord['CVotes3044M'].iloc[0]
    m4 = movieRecord['CVotes45AM'].iloc[0]
    total = f1+f2+f3+f4+m1+m2+m3+m4 # calculate the total number of voters
    yf = [f1/total, f2/total, f3/total, f4/total] # calculate percentage for female
    ym = [m1/total, m2/total, m3/total, m4/total] # calculate percentage for male
    
    plt.figure() # start a new plot
    plt.bar(xf, yf, color = 'pink', align='edge') # bar chart for female
    for i in range(len(xf)): # add annotate for each bar
        plt.annotate(format(yf[i], '4.1%'), (xf[i], yf[i]))
        
    plt.bar(xm, ym, color = 'lightgreen', align='edge') # bar chart for male
    for i in range(len(xm)): # add annotate for each bar
        plt.annotate(format(ym[i], '4.1%'), (xm[i], ym[i]))
    
    plt.xticks(rotation = 30) # rotate the x-axis values displayed
    plt.ylabel('% of raters')
    plt.title('Percentage of raters within gender-age group for \''+movieTitle+'\'')    
    plt.savefig('plot2.jpg')
    
    return

def main():
    folderName = input('Please enter the name of the subfolder with the data file: ')
    movieDFForPlot1 = pickMovieWithKeyword(folderName)
    plot1(movieDFForPlot1)
    
    print('\n\n'+str('-'*80)+'\n')
    
    plot2() 
    
    return

main()
