phrase = input()

words_list = ["dream", "dreamer", "erase", "eraser"]
reversed_words_list = [ word[::-1] for word in words_list ]
reversed_phrase = phrase[::-1]

can1 = True
for i in range(len(reversed_phrase)):
    can2 = False
    if len(reversed_phrase) == 0:
        can2 = True
        break
    for checker in reversed_words_list:
        if reversed_phrase[0:len(checker)] == checker:
            can2 = True
            reversed_phrase = reversed_phrase[len(checker):]
            break
    if not can2:
        can1 = False
        break

if can1:
    print("YES")
else:
    print("NO")


# reference
# words_list = ["dream", "dreamer", "erase", "eraser"]
# reversed_words_list = [ word[::-1] for word in words_list ]
# reversed_five_letters_words_list = [ word[0:5] for word in reversed_words_list ]
# reversed_five_letters_words_list = [ word[-1:-6:-1] for word in words_list ]
