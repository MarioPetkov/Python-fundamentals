num_of_words = int(input())
special_word = input()
words_list = []
special_list = []
for i in range(num_of_words):
    word = input()
    words_list.append(word)
    if special_word in word:
        special_list.append(word)
print(words_list)
print(special_list)
