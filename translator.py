
def translate_phrase(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                 translation = translation + "g"
        else:
            translation = translation + letter
    return translation

phrase = input("Enter the phrase: ")
print("The translated phrase is " + translate_phrase(phrase))

# This is comment

'''
These are comments.
'''