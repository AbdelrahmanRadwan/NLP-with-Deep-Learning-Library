def tokenize_max_match(dictionary, input):
    start = 0
    counter = 0
    while start < len(input):
        Max_len=0
        token = "empty string"
        for word in dictionary:

            if len(word)>len(input)-start:
                continue
            if input[start:start + len(word)] == word and len(word)>=Max_len:
                Max_len = len(word)
                token = word

        start+=Max_len
        print (token)
