dictionary = {}

while True:
    word = raw_input("Please enter a word: ")
    if word == "":
        break
    if word in words:
        dictionary[word] +=1
        print "Seen that ", dictionary[word], "times"
    else:
        dictionary[word] = 1
        print "That's a new word."
