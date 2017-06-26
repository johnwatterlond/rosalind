"""
Program to solve the Rosalind problem at rosalind.info/problems/prot/

"""

codon_dict = dict([('UGA', 'Stop'), ('GGA', 'G'), ('CAU', 'H'), ('CAA', 'Q'), ('UGC', 'C'), ('AAG', 'K'), ('GUU', 'V'), ('UAA', 'Stop'), ('GAG', 'E'), ('CGA', 'R'), ('AGG', 'R'), ('AAU', 'N'), ('UGG', 'W'), ('CCG', 'P'), ('UUG', 'L'), ('GUG', 'V'), ('GAU', 'D'), ('GCG', 'A'), ('AAA', 'K'), ('ACC', 'T'), ('AUC', 'I'), ('CCC', 'P'), ('UCC', 'S'), ('CGG', 'R'), ('CGU', 'R'), ('UAG', 'Stop'), ('CCU', 'P'), ('GCU', 'A'), ('AUU', 'I'), ('AGC', 'S'), ('AUG', 'M'), ('UCA', 'S'), ('GUC', 'V'), ('CUC', 'L'), ('CAG', 'Q'), ('UUU', 'F'), ('ACA', 'T'), ('AGA', 'R'), ('GGG', 'G'), ('CUU', 'L'), ('GGC', 'G'), ('CAC', 'H'), ('GGU', 'G'), ('AAC', 'N'), ('UUA', 'L'), ('CGC', 'R'), ('UAC', 'Y'), ('GAC', 'D'), ('UCU', 'S'), ('GCA', 'A'), ('GCC', 'A'), ('CCA', 'P'), ('AUA', 'I'), ('GUA', 'V'), ('CUG', 'L'), ('CUA', 'L'), ('UGU', 'C'), ('ACU', 'T'), ('UAU', 'Y'), ('AGU', 'S'), ('GAA', 'E'), ('UCG', 'S'), ('UUC', 'F'), ('ACG', 'T')])


def rna_to_prot(s):
    """Convert RNA string s to protien string using codon_dict."""
    triples = list(map(''.join, zip(*[iter(s)]*3))) # from doc for zip().
    trans = [codon_dict[triple] for triple in triples]
    return ''.join([x for x in trans if x != 'Stop'])


def solve_problem(s):
    """Create file '../output/prot_answer.txt' containing solution."""
    fout = open('../output/prot_answer.txt', 'w')
    fout.write(rna_to_prot(s))
    fout.close()


def main():
    location = '../datasets/rosalind_prot.txt'
    fin = open(location)
    s = fin.read().strip()
    solve_problem(s)
    fin.close()


if __name__ == '__main__':
    main()
