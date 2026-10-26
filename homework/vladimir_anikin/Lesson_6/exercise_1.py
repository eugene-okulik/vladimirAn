text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()
m_words = []
for word in words:
    if "," in word or "." in word:
        c_word = word.strip(",.")
        punctuation = word[len(c_word) :]
        n_word = c_word + "ing" + punctuation
        m_words.append(n_word)
    else:
        ing_word = word + "ing"
        m_words.append(ing_word)
print(" ".join(m_words))
