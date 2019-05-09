'''
Created on Dec 1, 2018

Rating-based movie recommendation

@author: lufei Guan
'''

def findClosestCritics(criticsRatingDF, personalRatingDF):
    import pandas as pd
    import math
    matchedMovieDF = pd.merge(personalRatingDF, criticsRatingDF) # merge the two DFs together with matched movies
    matchedMovieDF.index = list(matchedMovieDF.loc[:,'Title']) # set Title as index
    matchedMovieDF.drop(columns = ['Title'], inplace = True) # drop Title column
       
    y = list(matchedMovieDF.iloc[:,0]) # get a list of personal rating values

    criticsListDF = pd.DataFrame(index = matchedMovieDF.columns[1:], columns = ['Euclidean']) # create an empty DF to record euclidean for each critics
    
    for i in range(matchedMovieDF.shape[1]-1): # calculate euclidean distance for each critics vs. personal
        x = list(matchedMovieDF.iloc[:,i+1])
        sqrsum = 0
        for j in range(matchedMovieDF.shape[0]):
            sqrsum = sqrsum + (x[j] - y[j])**2
            j += 1
        Euclidean = math.sqrt(sqrsum)
        criticsListDF.iloc[i,0] = Euclidean # assign euclidean values to DF
        i += 1
    
    criticsListDF = criticsListDF.sort_values(by = ['Euclidean']) # sort critics by Euclidean distance in ascending order
    criticsList = list(criticsListDF.index[:3])
     
    return criticsList


def recommendMovies(personalRatingDF, criticsRatingDF, criticsList, movieDF):
    import pandas as pd
    
    movieDF.index = list(movieDF.loc[:,'Title']) # set Title as index
    movieDF = pd.DataFrame(movieDF, columns = ['Title','criticsRating','Genre1','Year','Runtime'])
    
    criticsRatingDF.index = list(criticsRatingDF.loc[:,'Title']) # set Title as index
    criticsRatingDF = pd.DataFrame(criticsRatingDF, columns = criticsList) # extract data for 3 critics

    movieDF.criticsRating = list(criticsRatingDF.mean(axis = 1)) # calculate average rating for each movie

    personalRatingDF.index = list(personalRatingDF.loc[:,'Title']) # set Title as index

    unwatchedMovie = movieDF.index.difference(personalRatingDF.index) # get unwatched movies
    unwatchedMovieDF = movieDF.reindex(index = unwatchedMovie)

    TopRatedDF= unwatchedMovieDF.groupby(by = 'Genre1', as_index = False)['criticsRating'].max() # get top 1 rating movie for each genre
    
    TopRatedUnwatchedDF = pd.merge(unwatchedMovieDF,TopRatedDF) # merge with the unwatched movie list
    TopRatedUnwatchedDF = TopRatedUnwatchedDF.sort_values(by = ['Genre1']) # sort by genre
    
    return TopRatedUnwatchedDF

   
def printRecommendations(TopRatedUnwatchedDF, personName):
    import pandas as pd
       
    print('Recommendations for', personName, ':')
    
    maxLengthOfTitle = max(TopRatedUnwatchedDF['Title'].apply(len)) # get max length of title
 
    for i in range(TopRatedUnwatchedDF.shape[0]): # print each row
        title = TopRatedUnwatchedDF.iloc[i,0]
        genre = TopRatedUnwatchedDF.iloc[i,2]
        rating = round(TopRatedUnwatchedDF.iloc[i,1], 2)
        year = TopRatedUnwatchedDF.iloc[i,3]
         
        if pd.isnull(TopRatedUnwatchedDF.iloc[i,4]):
            print(('"'+title+'"').ljust(maxLengthOfTitle+2),
                  '('+genre+'), rating:', str(rating)+',', str(year))
        else:
            runtime = TopRatedUnwatchedDF.iloc[i,4]
            print(('"'+title+'"').ljust(maxLengthOfTitle+2),
                  '('+genre+'), rating:', str(rating)+',', str(year)+', runs', runtime)
           
    return 
        
  
def main():
    import os
    import pandas as pd
       
    str = input('Please enter the name of the folder with files, the name of movies file,\nthe name of critics file, the name of personal ratings file, separated by spaces:\n')
    l = list(str.split())
       
    os.chdir(os.getcwd()+'\\'+l[0])
       
    movieDF = pd.read_csv(l[1], encoding = 'latin1')
    criticsRatingDF = pd.read_csv(l[2], encoding = 'latin1')
    personalRatingDF = pd.read_csv(l[3], encoding = 'latin1')
       
    criticsList = findClosestCritics(criticsRatingDF, personalRatingDF)
    print('\n',criticsList,'\n')
       
    TopRatedUnwatchedDF = recommendMovies(personalRatingDF, criticsRatingDF, criticsList, movieDF)
      
    personName = personalRatingDF.columns[1]
    printRecommendations(TopRatedUnwatchedDF, personName)
   
    return
   
main()
