#
# ps7pr5.py (Problem Set 7, Problem 5)
#
# TT Securities
#
# Computer Science 111
#
import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the min and its day')
    print('(6) Find the max and its day')
    print('(7) Test the threshold')
    print('(8) Your TT investment plan')
    print('(9) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """

    print('Day', 'Prices')
    print('---', '-----')
    for i in range(len(prices)):
        print('%3.0f' % i, prices[i])
        

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your helper functions for options 3-8 below.
def average(prices):
    '''Returns the average price of the values'''
    total = 0
    for i in range(len(prices)):
        total += prices[i]
        average= total // (i+1)

    return(average)

def standard(prices):
    '''Finds the standard deviation given the prices'''
    sum_of_values = 0
    for i in prices:
        sum_of_values += (i-average(prices)) ** 2
        final = math.sqrt(sum_of_values // len(prices))

    print('The standard deviation is', final)       
    

def min_day(prices):
    '''Finds the lowest price and the day it is on'''
    day = 0
    lowest = prices[0]
    for i in range(len(prices)):
        if lowest > prices[i]:
            lowest = prices[i]
            day = i
        else:
            day = day
            lowest = lowest
    print('The min price is', lowest, 'on day', day)

def max_day(prices):
    '''Finds the highest price and which day it is on'''
    day = 0
    greatest = prices[0]
    for i in range(len(prices)):
        if greatest < prices[i]:
            greatest = prices[i]
            day = i
        else:
            day = day
            greatest = greatest
    print('The max price is', greatest, 'on day', day)


def threshold_eq(prices):
    '''Finds if there are any values greater than the threshold entered'''
    threshold = int(input('Enter the Threshold: '))
    for i in prices:
        if threshold < i:
            print('There is at least one price over', threshold)
            return
                    
    print('There are no prices over', threshold)

def time_travel(prices):
    '''Finds the lowest price to buy in the 'past' and looks for the
highest price to sell in the 'future'''
    low = prices[0]
    great = 0
    diff = 0
    for i in range(len(prices)):
        for y in range(i,len(prices)):
            if prices[y] - prices[i] > diff:
                low = prices[i]
                great = prices[y]
                diff = prices[y] - prices[i]
                minday = i
                maxday = y

    print('Buy on day', minday, 'at price', low)
    print('Sell on day', maxday, 'at price', great)
    print('Total profit:', diff)
                
                

    
def tts():
    """ the main user-interaction loop
    """
    prices = []
    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 9:
            break
        elif choice < 9 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            print('The average price is', average(prices))
        elif choice == 4:
            standard(prices)
        elif choice == 5:
            min_day(prices)
        elif choice == 6:
            max_day(prices)
        elif choice == 7:
            threshold_eq(prices)
        elif choice == 8:
            time_travel(prices)

            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
