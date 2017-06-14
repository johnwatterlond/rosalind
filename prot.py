"""
Program to solve the Rosalind problem at rosalind.info/problems/prot/

"""


codon_dict = dict([('UGA', 'Stop'), ('GGA', 'G'), ('CAU', 'H'), ('CAA', 'Q'), ('UGC', 'C'), ('AAG', 'K'), ('GUU', 'V'), ('UAA', 'Stop'), ('GAG', 'E'), ('CGA', 'R'), ('AGG', 'R'), ('AAU', 'N'), ('UGG', 'W'), ('CCG', 'P'), ('UUG', 'L'), ('GUG', 'V'), ('GAU', 'D'), ('GCG', 'A'), ('AAA', 'K'), ('ACC', 'T'), ('AUC', 'I'), ('CCC', 'P'), ('UCC', 'S'), ('CGG', 'R'), ('CGU', 'R'), ('UAG', 'Stop'), ('CCU', 'P'), ('GCU', 'A'), ('AUU', 'I'), ('AGC', 'S'), ('AUG', 'M'), ('UCA', 'S'), ('GUC', 'V'), ('CUC', 'L'), ('CAG', 'Q'), ('UUU', 'F'), ('ACA', 'T'), ('AGA', 'R'), ('GGG', 'G'), ('CUU', 'L'), ('GGC', 'G'), ('CAC', 'H'), ('GGU', 'G'), ('AAC', 'N'), ('UUA', 'L'), ('CGC', 'R'), ('UAC', 'Y'), ('GAC', 'D'), ('UCU', 'S'), ('GCA', 'A'), ('GCC', 'A'), ('CCA', 'P'), ('AUA', 'I'), ('GUA', 'V'), ('CUG', 'L'), ('CUA', 'L'), ('UGU', 'C'), ('ACU', 'T'), ('UAU', 'Y'), ('AGU', 'S'), ('GAA', 'E'), ('UCG', 'S'), ('UUC', 'F'), ('ACG', 'T')])


def rna_to_prot(s):
    """Convert rna string s to protien string using codon_dict."""
    s_broken = map(''.join, zip(*[iter(s)]*3)) # from docs for zip().
    triples = [x for x in s_broken]
    trans = [codon_dict[x] for x in triples]
    return ''.join([x for x in trans if x != 'Stop'])


def solve_problem(s):
    """Create file in cwd 'prot_answer.txt' containing solution."""
    fout = open('prot_answer.txt', 'w')
    fout.write(rna_to_prot(s))
    fout.close()


def main():
    f = input('Location of rosalind_prot.txt?\n> ')
    s = open(f).read().strip()
    solve_problem(s)


if __name__ == '__main__':
    main()
