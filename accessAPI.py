import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

book = input("Which book of the Book of Mormon would you like? ")
chapter = input("Which chapter of " + book + " are you interested in? ")


complete_url = base_url + book + "/" + chapter

response = requests.get(complete_url)

data = response.json()

summary = data['chapter']['summary']

# Print the summary
print("Summary of " + book + " chapter " + chapter + ":")
print(summary)

# Ask the user if they want to view another chapter
view_another = input("Would you like to view another (Y/N)? ")
if view_another.lower() == 'n':
    print("Thank you for using Book of Mormon Summary Tool!")
