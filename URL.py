
import pyshorteners

# initialize the shortener
s = pyshorteners.Shortener()

# get the original URL from the user
long_url = input("Enter the URL to shorten: ")

# shorten the URL using TinyURL service
short_url = s.tinyurl.short(long_url)

# print the shortened URL
print("Shortened URL:", short_url)