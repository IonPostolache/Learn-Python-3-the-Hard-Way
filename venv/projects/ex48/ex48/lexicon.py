# lexicon:
Direction_words= ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
Verbs= ["go", "stop", "kill", "eat"]
Stop_words= ["the", "in", "of", "from", "at", "it"]
Nouns= ["door", "bear", "princess", "cabinet"]
Numbers= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def scan(s):
    stuff = input('> ')
    words = stuff.split()
    print(f"You entered the words: {words}")

    first = words[0]
    print(f"The first word is: {first}.")
    second=words[1]
    print(f"The second word is: {second}.")
    third=words[2]
    print(f"The third word is: {third}.")
    if first in Direction_words:
        first_propr="direction"
        print(f"The first word is a {first_propr}.")
    elif first in Verbs:
        first_propr="verb"
        print(f"The first word is a {first_propr}.")
    elif first in Stop_words:
        first_propr="stop word"
        print(f"The first word is a {first_propr}.")
    elif first in Nouns:
        first_propr="noun"
        print(f"The first word is a {first_propr}.")
    elif first in Numbers:
        first_propr="number"
        print(f"The first word is a {first_propr}.")
    else:
        print("This word is not an accepted word!")

    print()



scan(1)

# this is the end result:
first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word[1], second_word[1], third_word[1]]
print(f"The rebuild sentence is: {sentence}.")



class Room1(object):

    def __init__(self, name, description):
        self.name = name
        self.description=description

    def scan(s, t):
        stuff = input('> ')
        words = stuff.split()
        print(f"{words}")


        #this is the end result:
        first_word = ('verb', 'go')
        second_word = ('direction', 'north')
        third_word = ('direction', 'west')
        sentence = [first_word, second_word, third_word]
        print(f"{sentence}")

    def convert_number(s):
        try:
            return int(s)
        except ValueError:
            return None







class Room2(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


        
class Room3(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)