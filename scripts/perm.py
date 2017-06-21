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
    return [perm for perm in perms]


def solve_problem(n):
    """Create file in cwd 'perm_answer.txt' containing solution."""
    fout = open('perm_answer.txt', 'w')
    perms = perms_of_len_n(n)

    fout.write(str(num_perms(n)))
    fout.write('\n')

    for perm in perms:
        fout.write(' '.join(map(str, perm)))
        fout.write('\n')

    fout.close()


def main():
    location = input('Location of rosalind_perm.txt?\n> ')
    n = open(location).read().strip()
    solve_problem(int(n))


if __name__ == '__main__':
    main()