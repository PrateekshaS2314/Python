def word_count(sen):
    words = sen.split()
    total = len(words)
    word_freq = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in word_freq:
            word_freq[word_lower] += 1
        else:
            word_freq[word_lower] = 1
    return total, word_freq

sentence = input("Enter sentence: ")
total, freq = word_count(sentence)

print("Total words:", total)
print("Word frequencies:", freq)
