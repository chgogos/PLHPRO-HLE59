zen_txt = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Ερώτημα α
def capitalize_keep_only_en_chars(word):
    # βοηθητική συνάρτηση που επιστρέφει ως κεφαλαία μόνο τους
    # αγγλικούς χαρακτήρες της συμβολοσειράς εισόδου word
    en_txt = ""
    for ch in word.upper():
        if ord("A") <= ord(ch) <= ord("Z"):
            en_txt += ch
    return en_txt


# Ερώτημα β
def tokenize(txt):
    # συνάρτηση που "σπάει" το κείμενο txt σε λέξεις απορρίπτοντας
    # χαρακτήρες που δεν είναι γράμματα του αγγλικού αλφαβήτου,
    # επιστρέφει λίστα με λέξεις με κεφαλαία γράμματα
    words = []
    for a_word in txt.split():
        words.append(capitalize_keep_only_en_chars(a_word))
    return words


# Ερώτημα γ
def char_frequencies(word_list):
    # συνάρτηση που επιστρέφει ένα λεξικό με το πλήθος εμφάνισης
    # κάθε χαρακτήρα στη λίστα συμβολοσειρών word_list
    alphabet = {}
    for w in word_list:
        for ch in w:
            alphabet[ch] = alphabet.get(ch, 0) + 1
    return alphabet


# Ερώτημα δ
def word_frequencies(word_list):
    # συνάρτηση που επιστρέφει λεξικό με το πλήθος εμφάνισης κάθε λέξης
    # στη λίστα συμβολοσειρών word_list
    word_freq = {}
    for w in word_list:
        word_freq[w] = word_freq.get(w, 0) + 1
    return word_freq


### Κυρίως πρόγραμμα ###

# Ερώτημα ε
words = tokenize(zen_txt)

# Ερώτημα ε1
histogram = char_frequencies(words)
total = sum(histogram.values())
print("Συχνότητα εμφάνισης γραμμάτων")
for item in sorted(histogram.items()):
    print("{}: {:.2f}%".format(item[0], item[1] * 100 / total))

# Ερώτημα ε2
w_freq = word_frequencies(words)
print("Λέξεις με πάνω από 3 γράμματα")
count = 1
freq_10 = 0
for item in sorted(w_freq, key=w_freq.get, reverse=True):
    if len(item) > 3:
        if count > 10 and freq_10 > w_freq[item]:
            break
        print(count, item, w_freq[item])
        if count == 10:
            freq_10 = w_freq[item]
        count += 1
