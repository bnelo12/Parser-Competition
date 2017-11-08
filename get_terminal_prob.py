import nltk
from nltk.corpus import treebank
from nltk.corpus import brown
# from nltk.book import text6 as MH

# tagged_MH = nltk.pos_tag(MH, tagset="universal")

with open('allowed_words.txt') as f:
    freq_table = {};
    for line in open('allowed_words.txt'):
        freq_table[line.rstrip('\n')] = {}; 

for word in treebank.tagged_words(): # + tagged_MH:
    if word[0] in freq_table:
       pos = word[1]
       if pos in freq_table[word[0]]:
            freq_table[word[0]][pos] += 1
       else:
            freq_table[word[0]][pos] = 1

vocab_file = open('vocab_test.gr', 'w')
for word in freq_table:
    if not freq_table[word]:
        print word
    for pos in freq_table[word]:
        vocab_file.write("{:<10}{:<10}{}\n".format(freq_table[word][pos], pos, word))

vocab_file.close()
