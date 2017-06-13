"""
Program to solve the Rosalind problem at rosalind.info/problems/rna/

"""

def dna_str_to_rna_str(s):
    """Convert DNA string s to RNA string."""
    return s.replace('T', 'U')


def solve_problem(s):
    """Create file in cwd 'rna_answer.txt' containing solution."""
    fout = open('rna_answer.txt', 'w')
    fout.write(dna_str_to_rna_str(s))
    fout.close()


def main():
    f = input('Location of rosalind_rna.txt?\n> ')
    s = open(f).read().strip()
    solve_problem(s)


if __name__ == '__main__':
    main()
