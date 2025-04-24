
def get_num_words(text):
    num_words = 0
    word_list = text.split()

    for words in word_list:
        num_words += 1

    return num_words


def character_count(text):
    characters_in_text = {}
    text = (text.lower())
    for characters in text:
        characters_in_text[characters] = characters_in_text.get(characters, 0) + 1
    return characters_in_text

def sort(characters_in_text):
    sorted_characters = []
    for key in characters_in_text:
        count = characters_in_text[key]
        new_characters_in_text = {}
        new_characters_in_text["character"] = key
        new_characters_in_text["number"] = count
        sorted_characters.append(new_characters_in_text)
    sorted_characters.sort(reverse=True, key=lambda d: d["number"])
    return sorted_characters