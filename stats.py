def get_num_words(content):
    count = len(content.split())
    return count

def get_num_characters(content):
    lower = content.lower()
    char_counts = {}
    for char in lower:
        if char not in char_counts:
            char_counts[char]=1
        else:
            char_counts[char]+=1
    return char_counts

def report(letter_counts):
    # Convert dictionary items to list of tuples
    l = list(letter_counts.items())
    l.sort(key=lambda x: x[1], reverse=True)
    print("--------- Character Count --------")
    for letter, count in l:
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")
    
    