words = []

while len(words) < 5:
    num = len(words) + 1
    word = input(f'Choose word number {num} ')
    words.append(word)

for word in words:

    word = word.lower()

    if len(word) > 1 and word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome.")
