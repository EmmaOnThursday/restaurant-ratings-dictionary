import sys
filename = sys.argv[1]


def alpha_sort_dictionary(filename):
    """Given a file of restaurant data, prints an alpha-sorted list of restaurant name and rating. """

    restaurant_data = open(filename)
    ratings = {}
    
    for line in restaurant_data:
        line = line.rstrip()
        line = line.split(":")
        ratings[line[0]] = line[1]
    
    restaurant_data.close()
    
    new_restaurant = raw_input("Enter a restaurant name.>> ")
    new_rating = raw_input("Enter a rating for {}.>> ".format(new_restaurant))
    ratings[new_restaurant] = new_rating

    keys = sorted(ratings)

    #iterate through to print restaurants & ratings alphabetically
    for item in keys:
        print item + " is rated at " + ratings[item] + "."

def sort_user_reported_rating(filename):
    """"""
    user_name = raw_input("Hello. What's your name?>> ")

    restaurant_data = open(filename)
    ratings = {}
    
    for line in restaurant_data:
        line = line.rstrip()
        line = line.split(":")
        ratings[line[0]] = line[1]
    
    restaurant_data.close()

    random_restaurant = ratings.popitem()
    print random_restaurant[0] + " is rated at " + random_restaurant[1] + "."
    # user_rating = raw_input("")


alpha_sort_dictionary(filename)
sort_user_reported_rating(filename)