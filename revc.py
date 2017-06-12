"""
Program to solve the Rosalind problem at rosalind.info/problems/revc/

"""

def reverse_string(s):
    """Returns the reverse of string s."""
    return s[::-1]


def complement(s):
    """Returns the DNA complement of string s."""
    l1 = list(s)
    for i, l in enumerate(l1):
        if l == 'A':
            l1[i] = 'T'
        elif l == 'T':
            l1[i] = 'A'
        elif l == 'C':
            l1[i] = 'G'
        elif l == 'G':
            l1[i] = 'C'
    return ''.join(l1)


def solve_problem(s):
    """Create file in cwd 'revc_answer.txt' containing solution."""
    fout = open('revc_answer.txt', 'w')
    fout.write(complement(reverse_string(s)))
    fout.close()


def main():
    f = input('Location of rosalind_revc.txt?\n> ')
    s = open(f).read().strip()
    solve_problem(s)


if __name__ == '__main__':
    main()
