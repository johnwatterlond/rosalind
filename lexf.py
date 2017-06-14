"""
Program to solve the Rosalind problem at rosalind.info/problems/lexf/

"""

import itertools


def all_strings(s, n):
    """
    Return list of all strings of length n that can be formed with
    letters from string s.
    Returned list is in lexicographic order.
    """
    prods = itertools.product(list(s), repeat=n)
    l = [x for x in prods]
    return [''.join(x) for x in l]


def solve_problem(s, n):
    """Create file in cwd 'lexf_answer.txt' containing solution."""
    fout = open('lexf_answer.txt', 'w')
    l = all_strings(s, n)
    for x in l:
        fout.write(x)
        fout.write('\n')
    fout.close()


def main():
    location = input('Location of rosalind_lexf.txt?\n> ')
    fin = open(location)
    raw_s = fin.readline().strip()
    n = int(fin.readline().strip())
    s = ''.join(raw_s.split(' '))
    solve_problem(s, n)


if __name__ == '__main__':
    main()
