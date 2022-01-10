rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },

    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'north': 'Hidden Chamber',
        'item': 'potion'
    },

    'Garden': {
        'north': 'Dining Room'
    },

    'Hidden Chamber': {
        'south': 'Dining Room',
        'item': 'extra life'
    }

}
