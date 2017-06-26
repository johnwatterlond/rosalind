"""
Program to solve the Rosalind problem at rosalind.info/problems/perm/

"""

import math
import itertools


def num_perms(n):
    """Return number of permutations of first {1, 2, ..., n}."""
    return math.factorial(n)


def perms_of_len_n(n):
    """Return list of all permutations of length n."""
    perms = itertools.permutations(list(range(1, n + 1)))
    return list(perms)


def format_perm_to_str(perm):
    """
    Convert permutation perm into string with elements
    separated by a space.
    """
    return ' '.join(map(str, perm))


def solve_problem(n):
    """Create file '../output/perm_answer.txt' containing solution."""
    fout = open('../output/perm_answer.txt', 'w')
    perms = perms_of_len_n(n)

    fout.write(str(num_perms(n)))
    fout.write('\n')

    for perm in perms:
        fout.write(format_perm_to_str(perm))
        fout.write('\n')

    fout.close()


def main():
    location = '../datasets/rosalind_perm.txt'
    fin = open(location)
    n = fin.read().strip()
    solve_problem(int(n))
    fin.close()


if __name__ == '__main__':
    main()
