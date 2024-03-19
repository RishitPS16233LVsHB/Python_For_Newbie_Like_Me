def replace_blank_with_hyphen(sentence):
    return sentence.replace(" ", "-")

sentence = input("Enter sentence: ")
print("Modified sentence:", replace_blank_with_hyphen(sentence))
