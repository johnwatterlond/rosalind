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
    prod = itertools.product(list(s), repeat=n)
    return [''.join(x) for x in prod]


def solve_problem(s, n):
    """Create file '../output/lexf_answer.txt' containing solution."""
    fout = open('../output/lexf_answer.txt', 'w')
    _all_strings = all_strings(s, n)
    for string in _all_strings:
        fout.write(string)
        fout.write('\n')
    fout.close()


def main():
    location = '../datasets/rosalind_lexf.txt'
    fin = open(location)
    raw_s = fin.readline().strip()
    n = int(fin.readline().strip())
    s = ''.join(raw_s.split(' '))
    solve_problem(s, n)
    fin.close()


if __name__ == '__main__':
    main()
