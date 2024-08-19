# import requests

# def get_random_book():
#     url = "https://api.freeapi.app/api/v1/public/books/book/random"

#     response = requests.get(url)
#     data = response.json()

#     if data['success'] and 'data' in data:
#         book_data = data['data']
#         input("To get your book, PRESS ENTER..")
#         volume_info = book_data.get('volumeInfo', {})
        
#         title = volume_info.get('title', 'No Title')
#         authors = volume_info.get('authors', ['Unknown Author'])  # authors is an array
#         description = volume_info.get('description', 'No Description')

  

#         print("\n",title,"~ by",", ".join(authors))
#         print("\n",description)
#         print()
# get_random_book()


import requests
def get_random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"

    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        book_data = data['data']
        # input("To get your book, PRESS ENTER..")
        title = book_data['volumeInfo']['title']
        authors = book_data['volumeInfo']['authors'] # authors is array
        description = book_data['volumeInfo']['description'] 

        return title,authors,description
    else:
        raise Exception('Failed to fech user data')
     
        

def main():
    try:
        title,authors,description = get_random_book()
        # print(title,"-",subtitle)
        print(title)
        print("by",*authors)
        print(description)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()