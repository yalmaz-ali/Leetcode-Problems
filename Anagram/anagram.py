import re

list_of_words = []
list_of_anagrams = []


def CleanWord(word: str):
    if '/' in word:
        words = word.split("/")
        cleanedWords = [re.sub("[^A-Za-z]", "", word) for word in words]
        return cleanedWords
    elif '-' in word:
        words = word.split("-")
        cleanedWords = [re.sub("[^A-Za-z]", "", word) for word in words]
        return cleanedWords
    else:
        return re.sub("[^A-Za-z]", "", word)


def uniqueList(list_: list):
    return list(set(list_))


def saveAnagram(index, word):
    list_anagrams = []

    list_1 = list(word)
    list_1.sort()
    for i, item in enumerate(list_of_words):
        if (index == i):
            continue
        list_2 = list(item)
        list_2.sort()
        if (list_1 == list_2):
            list_anagrams.append(word)
            list_anagrams.append(item)
    if (len(list_anagrams) > 0):
        list_anagrams.sort()
        list_anagrams = uniqueList(list_anagrams)
    return list_anagrams


with open('text_doc.txt', 'r') as f:
    doc = f.read()
    doc_words = doc.split()

for word in doc_words:
    cleanedWords = CleanWord(word)
    if isinstance(cleanedWords, list):
        for w in cleanedWords:
            if (len(w) > 1):
                list_of_words.append(w.lower())
    else:
        if (len(cleanedWords) > 1):
            list_of_words.append(cleanedWords.lower())

list_of_words = uniqueList(list_of_words)

for index, item in enumerate(list_of_words):
    anagramSet = saveAnagram(index, item)
    if (anagramSet and not (anagramSet in list_of_anagrams)):
        list_of_anagrams.append(anagramSet)

print(list_of_anagrams)
