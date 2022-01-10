#!/usr/bin/env python3

import requests
from pprint import pprint

# URL = "https://swapi.dev/api/people/four"
URL = "https://swapi.dev/api/people/4/"
URL2 = "https://swapi.dev/api/films/1/"
URL3 = "https://swapi.dev/api/starships/13/"


def main():
    resp = requests.get(URL)
    resp2 = requests.get(URL2)
    resp3 = requests.get(URL3)

    if resp.status_code == 200:
        vader = resp.json()
        # pprint(vader)
        print(f"{vader['name']} was born in the year {vader['birth_year']}. His eyes are now {vader['eye_color']} "
              f"and his hair color is {vader['hair_color']}.")
    else:
        print("That is not a valid URL.")

    films = resp2.json()
    ship = resp3.json()

    print(f"He first appeared in the movie {films['title']} and could be found flying around in his {ship['name']}.")


if __name__ == '__main__':
    main()
