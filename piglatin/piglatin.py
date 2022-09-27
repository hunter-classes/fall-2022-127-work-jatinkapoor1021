The following code works for uppercase as well, as per the hw from last week: 


def piglatin(word):
    
    word = word.lower()
    print(word)
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        word = word + 'yay'
    else:
        word = word[1:len(word)] + word[0] + 'ay'
    
    return word

print(piglatin('HELLO'))
print(piglatin('apple'))
print(piglatin('toy'))
    
