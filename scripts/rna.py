"""
Program to solve the Rosalind problem at rosalind.info/problems/rna/

"""

def dna_str_to_rna_str(dna_string):
    """Convert DNA string dna_string to RNA string."""
    return dna_string.replace('T', 'U')


def solve_problem(s):
    """Create file '../output/rna_answer.txt' containing solution."""
    fout = open('../output/rna_answer.txt', 'w')
    rna_string = dna_str_to_rna_str(s)
    fout.write(rna_string)
    fout.close()


def main():
    location = '../datasets/rosalind_rna.txt'
    fin = open(location)
    dna_string = fin.readline().strip()
    solve_problem(dna_string)
    fin.close()


if __name__ == '__main__':
    main()
