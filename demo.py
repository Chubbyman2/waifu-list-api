import json
import requests


def add_json(BASE, jsonpath, PASSWORD=None):
    '''
    Given a json file with a list of waifu entry dicts,
    insert all into the database.
    '''
    f = open(jsonpath)
    data = json.load(f)

    # For every waifu dict in the json file, POST an entry
    for waifu_dict in data:
        query = {
            "id": waifu_dict["id"],
            "name": waifu_dict["name"],
            "anime": waifu_dict["anime"],
            "rank": waifu_dict["rank"],
            "image": waifu_dict["image"],
            "password": PASSWORD
        }
        posted = requests.post(BASE + "waifulist", query).json()
        posted["image"] = "https://waifu-list-api.herokuapp.com/static/waifus/" + posted["image"]
        print(f"{posted['name']} entry posted.")
    
    print("All entries added.")


def get_all(BASE):
    '''
    Retrieves all entries from waifu_list table.
    This only works if you didn't delete any entries in between.
    Returns a list of all the entries in waifu_table.
    '''
    ret = []

    i = 1
    while True:
        retrieved = requests.get(BASE + "waifulist", params={"id": i}).json()
        try:
            retrieved["image"] = "https://waifu-list-api.herokuapp.com/static/waifus/" + retrieved["image"]
            print(f"{retrieved['name']} entry retrieved.")
            ret.append(retrieved)
            i += 1
        except KeyError:
            break

    print("All entries retrieved.")
    return ret


def delete_all(BASE, PASSWORD=None):
    '''
    Deletes all entries in the waifu_list table.
    This only works if you didn't delete any entries in between.
    '''
    i = 1
    while True:
        deleted = requests.delete(BASE + "waifulist", params={"id": i, "password": PASSWORD}).json()
        try:
            deleted["image"] = "https://waifu-list-api.herokuapp.com/static/waifus/" + deleted["image"]
            print(f"{deleted['name']} entry deleted.")
            i += 1
        except KeyError:
            break
    
    print("All entries deleted.")


def add_one(BASE, id, name, anime, rank, image, PASSWORD=None):
    '''
    All entry parameters are mandatory for POST, as defined in api.py.
    Inserts one entry into the database.
    image is the image path.
    '''
    query = {
        "id": id,
        "name": name,
        "anime": anime,
        "rank": rank,
        "image": image,
        "password": PASSWORD
    }

    posted = requests.post(BASE + "waifulist", query).json()
    try:
        posted["image"] = "https://waifu-list-api.herokuapp.com/static/waifus/" + posted["image"]
        print(f"{posted['name']} entry added.")
        return posted
    except KeyError: # For the abort cases (no/wrong password, missing param, etc)
        print(posted["message"])
        return posted


def delete_one(BASE, id=None, name=None, rank=None, PASSWORD=None):
    '''
    Only two parameters are needed for DELETE: id/name/rank and PASSWORD.
    Deletes the specified entry from the database.
    '''
    query = {
        "id": id,
        "name": name,
        "rank": rank,
        "password": PASSWORD
    }
    deleted = requests.delete(BASE + "waifulist", params=query).json()
    try:
        deleted["image"] = "https://waifu-list-api.herokuapp.com/static/waifus/" + deleted["image"]
        print(f"{deleted['name']} entry deleted.")
        return deleted
    except KeyError: 
        print(deleted["message"])
        return deleted


if __name__ == "__main__":
    BASE = "https://waifu-list-api.herokuapp.com/"
    PASSWORD = "your_password_here"




