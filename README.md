In our game we have to create a list of allowed words called a "lexicon":

Direction words: north, south, east, west, down, up, left, right, back
Verbs: go, stop, kill, eat
Nouns: door, bear, princess, cabinet
Numbers: any string of 0 through 9 characters

And the goal is to get as a result the following:

lexicon.scan("north", "eat", "door")

[('direction','north'), ('verb', 'eat'), ('noun','door')]
