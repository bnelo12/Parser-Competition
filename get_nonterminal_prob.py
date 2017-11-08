import nltk
from nltk.corpus import treebank

freq_count = {}

for sentence in treebank.parsed_sents():
    sentence.chomsky_normal_form()
    for production in sentence.productions():
        if production.is_nonlexical():
            lhs = production.lhs()
            rhs = production.rhs()
            if lhs in freq_count and rhs in freq_count[lhs]:
                freq_count[lhs][rhs]+=1
            else:
                freq_count[lhs] = {}
                freq_count[lhs][rhs] = 1

grammar_file = open('grammar_test.gr', 'w')
grammar_file.write('99 TOP S1\n')
grammar_file.write('1  Top  S2\n')

for nonterminal in freq_count:
    for prod in freq_count[nonterminal]:
        if len(prod) == 2:
            grammar_file.write('{} {} {}\n'.format(freq_count[nonterminal][prod], nonterminal.symbol().replace('#','HASxH, prod[0].replace('#', 'HASH'), prod[1].replace('#', 'HASH')))

            
