import nltk
from nltk.corpus import treebank
from nltk.grammar import CFG, Nonterminal

freq_count = {}

def replace_chars(string):
    string = string.replace("#", "HASH")
    string = string.replace(":", "COLON")
    string = string.replace(",", "COMMA")
    string = string.replace(".", "PERIOD")
    return string

for sent in treebank.parsed_sents():
    sent.chomsky_normal_form()
    for production in sent.productions():
        if production.is_nonlexical():
            lhs = production.lhs()
            rhs = production.rhs()
            if lhs in freq_count and rhs in freq_count[lhs]:
                freq_count[lhs][rhs]+=1
            elif lhs in freq_count:
                freq_count[lhs][rhs] = 1
            else:
                freq_count[lhs] = {}
                freq_count[lhs][rhs] = 1

grammar_file = open('grammar_test.gr', 'w')
grammar_file.write('99 TOP S\n')

for nonterminal in freq_count:
    for prod in freq_count[nonterminal]:
        if freq_count[nonterminal][prod] > 0:
            grammar_file.write('{} {} '.format(freq_count[nonterminal][prod], replace_chars(str(nonterminal))))
            for p in prod:
                grammar_file.write(replace_chars(str(p)) + " ")
            grammar_file.write("\n")

