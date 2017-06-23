"""
Program to solve the Rosalind problem at rosalind.info/problems/revc/

"""

def reverse_string(s):
    """Returns the reverse of string s."""
    return s[::-1]


def dna_complement(dna_string):
    """Returns the DNA complement of DNA string dna_string."""
    complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    mapping = str.maketrans(complement_dict)
    return dna_string.translate(mapping)


def reverse_complement(dna_string):
    """Return reverse complement of DNA string dna_string."""
    return dna_complement(reverse_string(dna_string))


def solve_problem(s):
    """Create file '../output/revc_answer.txt' containing solution."""
    fout = open('../output/revc_answer.txt', 'w')
    fout.write(reverse_complement(s))
    fout.close()


def main():
    location = '../datasets/rosalind_revc.txt'
    fin = open(location)
    dna_string = fin.readline().strip()
    solve_problem(dna_string)
    fin.close()


if __name__ == '__main__':
    main()
