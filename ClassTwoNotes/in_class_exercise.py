import user
import listing
import shop
import shop as s


file_path = "/Users/hoops/Dropbox/Practical Data Science/data files/ecommerce/"
user_filename = "users.json"
listings_filename = "listings.json"
shops_filename = "shops.json"

shops_file = open(file_path+shops_filename, 'r')
all_shops = []

for line in shops_file:
    new_shop = shop.fromJson(line)
    all_shops.append(new_shop)

shops_file.close()

user_file = open(file_path+user_filename, 'r')
all_users = []

for line in user_file:
    new_user = user.fromJson(line)
    all_users.append(new_user)
user_file.close()

listing_file = open(file_path+listings_filename, 'r')
all_listings = []

for line in listing_file:
    new_listing = listing.fromJson(line)
    all_listings.append(new_listing)

listing_file.close()


print "have " + str(len(all_shops)) + " shops"
print "have " + str(len(all_users)) + " users"
print "have " + str(len(all_listings)) + " listings"

num_friends = dict()
num_favorites = dict()
num_purchases = dict()

for a_user in all_users:
    num = len(a_user.favorites)

    if not num_favorites.has_key(num):
        num_favorites[num] = 1
    else:
        num_favorites[num] = num_favorites[num] + 1

        
print num_favorites

