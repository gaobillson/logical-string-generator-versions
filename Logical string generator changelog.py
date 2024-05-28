"""
LOGICAL STRING GENERATOR--CHANGELOG

V1 -This program generates a random string from different functions. Each letter is
 based on bi-grams, disregarding the probabilities of each letter. Each letter has an
 equal chance of being chosen. Each letter is based on the preceding letter. There
 is complete error handling. Press 'Enter' to repeat with the same settings,
 'e' to exit, or just enter new settings.

V2- Updated for each letter to have a different probability of being chosen. Based
 on the preceding letter, there is a certain set of letters which each have
 different probabilities of being chosen.

V3 - Used rounded probabilities to remove the least likely letters of being chosen.
 Also used random.uniform to choose floats.

V4 - Now makes 'sentences'. The length of each word is randomized from 1-13

V5 - Added probabilities for different word lengths. Two different sets of probabilities:
 1) Probabilities from Quora: https://www.quora.com/How-many-4-letter-words-exist-in-English
 2) Custom probabilities (because Quora's were based on a dictionary which had too many long words)
 Additionally limited sentence length to 20 words and made multi-line sentences if sentence
  is > 104 characters and > 10 words.
 Finally, the first letter of every word was not random. It was based on the last letter
  of the previous word. Now every first letter is truly random.

V6 - Integrated some 'rules' into the generator.
 The following 'unpronunciabilitites' were fixed:
    Three or more consecutive consonants
    Double consonants starting a word ('ss' and 'll' mostly)
    Consonants after 'y' when 'y' starts a word
    Double consonants after 'y' when 'y' doesn't start word
    Wholly consonant single- and double-letter words
    Consonant after 'qu'
 Additionally, some optimizations and tweaks were made:
    The first letter is now random.choice instead of using a separate function to do it.
    Optimized making new lines. Now it can generate 1-30 words in a sentence and
     fit 4 lines of text (rarely the case). Additionally, now it breaks lines more logically.
    Choosing 'random' for the sentence length randomizes between 1 and 30 words,
     not 5-20 as before.

V7 - Ultimate Logical String Generator: You can choose to use the sentence or word generator, all in one.
"""
string = "c"
current = "p"


def digraphs_checker():
    lax = len(string) - 1
    digraphs = ('bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl',
                'gr', 'ng', 'ph', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn',
                'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr')
    test = string + current
    if test[lax:lax + 2] in digraphs:
        return True
    else:
        return False


print(digraphs_checker())
