import requests


if __name__ == "__main__":
    '''
    There are three HTTP methods to check.
    This script is to ensure that POST, PUT, and DELETE all require passwords.
    '''
    # BASE = "https://waifu-list-api.herokuapp.com/"
    # PASSWORD = "your-password-here"

    # For local testing
    BASE = "http://127.0.0.1:5000/"
    PASSWORD = "Melanie"

    # POST
    test = requests.post(BASE + "waifulist", {"id": 52, "name": "your mom", "anime": "real life", "rank": 52, "image": "your_mom.png", "password": None}).json()
    print(test)

    # PUT
    test2 = requests.put(BASE + "waifulist", {"id": 51, "anime": "Fire Emblem Awakening"}).json()
    print(test2)

    # DELETE (remember that delete requires params={} to be specified)
    test3 = requests.delete(BASE + "waifulist", params={"id": 1}).json()
    print(test3)

    # GET (this should work without a password)
    test4 = requests.get(BASE + "waifulist", {"id": 1}).json()
    print(test4)

