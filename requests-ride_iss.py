#!/usr/bin/env python3

import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'


def main():
    groundctrl = requests.get(MAJORTOM)

    helmetson = groundctrl.json()

    print("\n\nConverted Python data")
    print(helmetson)
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    for person in people:
        print(f"{person['name']} on the {person['craft']}")


if __name__ == "__main__":
    main()
