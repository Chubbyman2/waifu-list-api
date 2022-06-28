import requests


if __name__ == "__main__":
    '''
    This script checks for whether mandatory params are working
    and aborts for things like repeat entry avoidance, deleting nonexistent entries, etc.
    '''

    # BASE = "https://waifu-list-api.herokuapp.com/"
    # PASSWORD = "your-password-here"

    # For local testing
    BASE = "http://127.0.0.1:5000/"
    PASSWORD = "Melanie"

    # POST - all params mandatory, so check each one individually
    test = requests.post(BASE + "waifulist", {"name": "your mom", "anime": "real life", "rank": 52, "image": "your_mom.png", "password": PASSWORD}).json()
    print(test)
    test2 = requests.post(BASE + "waifulist", {"id": 52, "anime": "real life", "rank": 52, "image": "your_mom.png", "password": PASSWORD}).json()
    print(test2)
    test3 = requests.post(BASE + "waifulist", {"id": 52, "name": "your mom", "rank": 52, "image": "your_mom.png", "password": PASSWORD}).json()
    print(test3)
    test4 = requests.post(BASE + "waifulist", {"id": 52, "name": "your mom", "anime": "real life", "image": "your_mom.png", "password": PASSWORD}).json()
    print(test4)
    test5 = requests.post(BASE + "waifulist", {"id": 52, "name": "your mom", "anime": "real life", "rank": 52, "password": PASSWORD}).json()
    print(test5)
    
    # POST - repeat entry check
    test6 = requests.post(BASE + "waifulist", {"id": 1, "name": "Mel Sievers", "anime": "Pulse", "rank": 1, "image": "mel_sievers.png", "password": PASSWORD}).json()
    print(test6)
    test7 = requests.post(BASE + "waifulist", {"id": 52, "name": "Lynn Wiles", "anime": "Pulse", "rank": 1, "image": "lynn_wiles.png", "password": PASSWORD}).json()
    print(test7)

    # PUT - id is the only mandatory parameter
    test8 = requests.put(BASE + "waifulist", {"name": "Mel Sievers", "anime": "Pulse", "rank": 1, "image": "mel_sievers.png", "password": PASSWORD}).json()
    print(test8)

    # DELETE - queries using either id, name, or rank (or any combination of the three)
    test9 = requests.delete(BASE + "waifulist", params={"anime": "Pulse", "image": "lynn_wiles.png", "password": PASSWORD}).json()
    print(test9)

    # DELETE - delete nonexistent entry check
    test10 = requests.delete(BASE + "waifulist", params={"id": 52, "password": PASSWORD}).json()
    print(test10)

    # GET - same query method as DELETE, so check for three params
    test11 = requests.get(BASE + "waifulist", params={"anime": "Pulse", "image": "lynn_wiles.png", "password": PASSWORD}).json()
    print(test11)
