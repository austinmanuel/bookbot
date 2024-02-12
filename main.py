def char_reps(contents):
    lowered = contents.lower()
    results = {}
    for char in lowered:
        if char.isalpha():
            if char in results:
                results[char] += 1
            else:
                results[char] = 1
    return sort_results(results)

def num_words(contents):
    words = contents.split()
    return len(words)

def sort_results(char_results):
    char_list = [(v, k) for k, v in char_results.items()]
    char_list.sort(reverse=True)
    return char_list

def report(nums, reps):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{nums} words found in the document")
    print("")
    for char in reps:
        print(f"The {char[1]} character was found {char[0]} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    nums = num_words(file_contents)
    reps = char_reps(file_contents)

    report(nums, reps)

if __name__ == "__main__":
    main()