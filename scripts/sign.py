"""
Program to solve the Rosalind problem at rosalind.info/problems/sign/

"""

import itertools


def perms_neg_n_to_n(n):
    """Returns a list of all perms of {-n, ..., -1, 1, ..., n}."""
    nums = list(range(-n, 0)) + list(range(1, n + 1))
    return itertools.permutations(nums, n)


def no_rep_pm(t):
    """
    Name is from: 'no repeats plus/minus'.
    Returns True if all elements in tuple t are unique modulo abs val.

    no_pm_rep((1, 2, -3)) --> True
    no_pm_rep((3, 2, -3)) --> False
    """
    return len(set(map(abs, t))) == len(t)


def signed_perms(n):
    """Return a list of all signed permutations of length n."""
    all_perms = perms_neg_n_to_n(n)
    return [perm for perm in all_perms if no_rep_pm(perm)]


def format_perm_to_str(perm):
    """
    Convert permutation perm into string with elements
    separated by a space.
    """
    return ' '.join(map(str, perm))


def solve_problem(n):
    """Create file '../output/sign_answer.txt' containing solution."""
    fout = open('../output/sign_answer.txt', 'w')
    perms = signed_perms(n)
    num_perms = len(perms)

    fout.write(str(num_perms))
    fout.write('\n')

    for perm in perms:
        fout.write(format_perm_to_str(perm))
        fout.write('\n')

    fout.close()


def main():
    location = '../datasets/rosalind_sign.txt'
    fin = open(location)
    n = fin.read().strip()
    solve_problem(int(n))
    fin.close()


if __name__ == '__main__':
    main()
