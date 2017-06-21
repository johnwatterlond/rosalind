"""
Program to solve the Rosalind problem at rosalind.info/problems/revc/

"""

def reverse_string(s):
    """Returns the reverse of string s."""
    return s[::-1]


def complement(s):
    """Returns the DNA complement of string s."""
    mapping = str.maketrans('ATCG', 'TAGC')
    return s.translate(mapping)


def reverse_complement(s):
    """Return reverse complement of DNA string s."""
    return complement(reverse_string(s))


def solve_problem(s):
    """Create file in cwd 'revc_answer.txt' containing solution."""
    fout = open('revc_answer.txt', 'w')
    fout.write(reverse_complement(s))
    fout.close()


def main():
    f = input('Location of rosalind_revc.txt?\n> ')
    s = open(f).read().strip()
    solve_problem(s)


if __name__ == '__main__':
    main()
