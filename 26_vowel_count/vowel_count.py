VOWELS = set("aeiou")

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # Original attempt, marked wrong by doctests for incorrect order of freq_map

    # lowercase = phrase.lower()
    # vowel_phrase =  [char for char in lowercase if 'aeiou'.find(char) != -1]
    # vowel_set = set(vowel_phrase)
    # freq_map = {}

    # for char in vowel_set:
    #     freq_map[char] = vowel_phrase.count(char)
    # return freq_map

    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter