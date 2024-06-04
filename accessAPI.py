import requests
import json

def get_book_id(book_name):
    url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon'
    response = requests.get(url)
    data = json.loads(response.text)
    for book in data['books']:
        if book['title'] == book_name:
            return book['_id']
    return None

def get_chapter_summary(book_id, chapter_num):
    url = f'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/{book_id}/{chapter_num}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['chapter']['summary']

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    book_name = input("Which book of the Book of Mormon would you like? ")
    book_id = get_book_id(book_name)
    if book_id is None:
        print(f"Sorry, {book_name} is not a valid book in the Book of Mormon.")
        return
    chapter_num = int(input(f"Which chapter of {book_name} are you interested in? "))
    summary = get_chapter_summary(book_id, chapter_num)
    print(f"Summary of {book_name} chapter {chapter_num}:\n{summary}")
    another = input("Would you like to view another (Y/N)? ")
    if another.upper() == 'Y':
        main()
    else:
        print("Thank you for using Book of Mormon Summary Tool!")

if __name__ == "__main__":
    main()
