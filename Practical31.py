def count_characters(text):
    total_characters = len(text)
    total_alphabets = sum(c.isalpha() for c in text)
    total_digits = sum(c.isdigit() for c in text)
    total_special_symbols = total_characters - total_alphabets - total_digits - text.count(" ")
    total_words = len(text.split())
    return total_characters, total_alphabets, total_digits, total_special_symbols, total_words

text = input("Enter text: ")
total_characters, total_alphabets, total_digits, total_special_symbols, total_words = count_characters(text)
print("Total characters:", total_characters)
print("Total alphabets:", total_alphabets)
print("Total digits:", total_digits)
print("Total special symbols:", total_special_symbols)
print("Total words:", total_words)
