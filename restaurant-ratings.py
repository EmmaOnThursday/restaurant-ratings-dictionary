import sys
filename = sys.argv[1]


def alpha_sort_dictionary(filename):
    """Given a file of restaurant data, prints an alpha-sorted list of restaurant name and rating."""

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
    """Given a file of restaurant data, asks user for restaurant name and rating and updates data."""
    
    raw_input("Hello. What's your name?>> ")

    restaurant_data = open(filename)
    ratings = {}
    
    for line in restaurant_data:
        line = line.rstrip()
        line = line.split(":")
        ratings[line[0]] = line[1]
    
    restaurant_data.close()

    while True: 
            random_restaurant = ratings.popitem()
            print random_restaurant[0] + " is rated at " + random_restaurant[1] + "."
            try:
                user_rating = int(raw_input("How would you rate {}? ".format(random_restaurant[0])))
            except ValueError:
                # if user_rating == 'q':
                ratings[random_restaurant[0]] = random_restaurant[1]
                break
            ratings[random_restaurant[0]] = user_rating

    keys = sorted(ratings)

    #iterate through to print restaurants & ratings alphabetically
    for item in keys:
        # print item + " is rated at " + ratings[item] + "."
        print"{} is rated at {}.".format(item, ratings[item])


# alpha_sort_dictionary(filename)
sort_user_reported_rating(filename)