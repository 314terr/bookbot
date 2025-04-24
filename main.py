import sys
from stats import get_num_words, character_count, sort

if len(sys.argv) != 2:
 print ("Usage: python3 main.py <path_to_book>")
 sys.exit(1) 

def main():

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    characters_in_text = character_count(text)
    sorted_characters = sort(characters_in_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for item in sorted_characters:
        if item["character"].isalpha():
         print (f"{item['character']}: {item['number']}")
           
          
    
    print("============= END ===============")


def get_book_text(path: str) -> str:
    with open(path) as file:
        text = file.read()

    return text

main()