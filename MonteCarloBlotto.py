#Created by Truman Daniels, Fall 2017
#The goal of this project is to figure out the optimal distribution of a 9 category fantasy basketball team


import random
import math



def gen_random_blotto():
    '''
    () ---> list
    generates a random strategy with 9 categories that add up to 100 (troops)

    '''
    blotto_list = []
    difference_list =[]
    
    for bf in range(8):
        blotto_list += [random.randint(0, 100)]
        
    blotto_list.sort(reverse=True)
    
    for bf in range(7):
        difference = blotto_list[bf] - blotto_list[bf+1]
        difference_list.append(difference)

    edge1 = 100 - blotto_list[0]
    edge2 = blotto_list[7] - 0
        
    difference_list.append(edge1)
    difference_list.append(edge2)

           
    #This algorithm that randomly assigns value 0-100 to each battlefield (category), with the total being no more than 100 Troops

    #there might be good reasons to changing the mean to 0 with an adjustment of -11.111111 to each category

    return difference_list


def single_test(strategy1, nopponents):
    '''
    (list, int) ---> float, list

    singletest lets you choose a strategy (a list with 9 elements which add up to 100)

    '''
        
    gameswon = 0 
    gameslost = 0
    for i in range (nopponents):                 #finds n different
              
        strategy2 = gen_random_blotto()
        categorieswon = 0        #number of statistical categories won by first strategy
        for bf in range(9):
            if random.gauss(strategy1[bf], 20) > random.gauss(strategy2[bf], 20):               #20 is chosen for variance because of the 82 games and roughly 4 games played per week
            #if strategy1[bf] > strategy2[bf]:
                categorieswon += 1
            else:
                None
            
        if categorieswon > 4:
            gameswon += 1
        else:
            gameslost += 1

    percent_win = gameswon/(gameswon + gameslost)

    #print statement examing how good of a strategy it is

    #print("A distribution of " + str(strategy1) + " won " + str(gameswon) + " and lost " + str(gameslost) + " games")
    #print("For a winning percentage of " + str(100*round(percent_win,3)) + "%")

    return (percent_win, strategy1)





def best_test(nstrategies, nopponents):     #algorithm might be improved speed-wise by comparing vs the same list of opponents
    '''
    (int, list) ---> none

    generates nstrategies random strategies and faces them each against nopponents number of opposing random strategies and finds the top 10

    ex:
    >>> best_test(10000, 10000)
    1
    2
    3
    .
    .
    .
    9998
    9999
    10000
    
    '''
    count = 0 
    list_strats = []
    for i in range(nstrategies):
        list_strats.append(single_test(gen_random_blotto(), nopponents))
        count += 1
        print(count)
    list_strats.sort(reverse=True)

    print(list_strats[0:10])

    




def direct_compare(strat1, strat2, games):
    '''
    (list, list, int) ---> float, list

    direct compare allows you to compare two different strategies and arrive a at win percentage for strategy 1 vs strategy 2

    ex:
    >>> direct_compare([11,11,11,11,11,11,11,11,12], [20, 0, 20, 0, 20, 0, 20, 0, 20], 1000000)
    (49.7477, [11, 11, 11, 11, 11, 11, 11, 11, 12])
    '''
    gameswon = 0 
    gameslost = 0
    for i in range (games):                
        categorieswon = 0        #number of statistical categories won by first strategy
        for bf in range(9):
            if random.gauss(strat1[bf], 20) > random.gauss(strat2[bf], 20):
            #if strategy1[bf] > strategy2[bf]:
                categorieswon += 1
            else:
                None
            
        if categorieswon > 4:
            gameswon += 1
        else:
            gameslost += 1

    percent_win = 100*gameswon/(gameswon + gameslost)


    return percent_win, strat1


