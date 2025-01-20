def pypy():
    letters = "abcdefghijklmnopqrstuvwxyz"
    char_count = {}
    # You don't need this empty count list
    # count = []  
    
    with open("books/frankenstein.txt") as f:
        text = f.read().lower()
        for letter in letters:
            char_count[letter] = text.count(letter)
        wordsplit = text.split()
        wordcount = len(wordsplit)
    
    char_list = []
    # This line had an error. Should be:
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})

    # Don't forget to add the sorting:
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    # Now let's print the report:
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document\n")
    
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")

pypy()