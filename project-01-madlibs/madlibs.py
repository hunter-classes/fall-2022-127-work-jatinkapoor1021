#EXTRAS:
#First extra completed:
#Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
#Second extra completed:
#Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.


import random


HERO = ['Elizabeth', 'Emily', 'Matthew', 'George', 'Angelina']
HERO_SELECTION = random.choice(HERO)

NOUNS = ['dog', 'monkey', 'cat', 'cow', 'donkey', 'horse']

VERBS = ['rotated', 'ran', 'danced', 'jumped', 'glided']

ADVERBS = ['boldly', 'quickly', 'cheerfully', 'awkwardly', 'bravely']


def replace_word(word):


    if "HERO" == word[1:-1]:

        return HERO_SELECTION

    if "NOUN" == word[1:-1]:

        return random.choice(NOUNS)        

    if "VERB" == word[1:-1]:

        return random.choice(VERBS)

    if "ADVERB" == word[1:-1]:

        return random.choice(ADVERBS)

    return word



def madlib(sentence):


    answer = ""

    for word in sentence.split():

        answer += " "

        if word[0] == "<" and word[-1] == ">":

            answer += replace_word(word)

        else:

            answer += word

    return answer


f = open('file.dat')
sentence = f.read()
print(madlib(sentence))
f.close()
