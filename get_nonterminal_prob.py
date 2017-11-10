import nltk
from nltk.corpus import treebank
from nltk.grammar import CFG, Nonterminal

freq_count = {}

for sent in treebank.parsed_sents():
    sent.chomsky_normal_form()
    for production in sent.productions():
        lhs = production.lhs()
        rhs = production.rhs()
        if lhs in freq_count and rhs in freq_count[lhs]:
            freq_count[lhs][rhs]+=1
        else:
            freq_count[lhs] = {}
            freq_count[lhs][rhs] = 1


grammar_file = open('grammar_test.gr', 'w')
grammar_file.write('99 TOP S\n')
grammar_file.write('1  Top  S2\n')

for nonterminal in freq_count:
    for prod in freq_count[nonterminal]:
        if len(prod) > 0:
            grammar_file.write('{} {} '.format(freq_count[nonterminal][prod], str(nonterminal.symbol()).replace("#", "-HASH-")))
            for p in prod:
                grammar_file.write(str(p).replace("#", "-HASH-") + " ")
            grammar_file.write("\n")
grammar_file.write("1   S2   Misc\n")
