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
    return len({x for x in map(abs, t)}) == len(t)


def signed_perms(n):
    """Return a list of all signed permutations of length n."""
    all_perms = perms_neg_n_to_n(n)
    return [perm for perm in all_perms if no_rep_pm(perm)]


def solve_problem(n):
    """Create file in cwd 'sign_answer.txt' containing solution."""
    fout = open('sign_answer.txt', 'w')
    perms = signed_perms(n)
    num_perms = len(perms)

    fout.write(str(num_perms))
    fout.write('\n')

    for p in perms:
        fout.write(' '.join(map(str, p)))
        fout.write('\n')

    fout.close()


def main():
    location = input('Location of rosalind_sign.txt?\n> ')
    n = open(location).read().strip()
    solve_problem(int(n))


if __name__ == '__main__':
    main()
